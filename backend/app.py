from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = "MY_SECRET_KEY"

# In-memory storage
users = []
tasks = []
task_id_counter = 1


# --------------------------- JWT ---------------------------
def generate_token(username, role):
    return jwt.encode(
        {
            "username": username,
            "role": role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        },
        app.config["SECRET_KEY"],
        algorithm="HS256"
    )


def verify_token():
    auth = request.headers.get("Authorization")
    if not auth:
        return None, None, "Missing token"

    try:
        token = auth.split(" ")[1]
        decoded = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        return decoded["username"], decoded["role"], None
    except Exception as e:
        return None, None, str(e)


# ----------------------- REGISTER --------------------------
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if any(u["username"] == data["username"] for u in users):
        return jsonify({"message": "User already exists"}), 400

    users.append({
        "username": data["username"],
        "password": data["password"],
        "role": data["role"]
    })

    return jsonify({"message": "User registered successfully"})


# ------------------------- LOGIN ---------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    for u in users:
        if u["username"] == data["username"] and u["password"] == data["password"]:
            token = generate_token(u["username"], u["role"])
            return jsonify({
                "message": "Login successful",
                "token": token,
                "role": u["role"],
                "username": u["username"]
            })

    return jsonify({"message": "Invalid username or password"}), 401


# ---------------------- CREATE TASK ------------------------
@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_counter

    username, role, error = verify_token()
    if error:
        return jsonify({"message": "Invalid token"}), 401

    data = request.get_json()

    task = {
        "id": task_id_counter,
        "title": data["title"],
        "description": data.get("description", ""),
        "due": data.get("due", ""),
        "status": "pending",
        "owner": username
    }

    tasks.append(task)
    task_id_counter += 1

    return jsonify({"message": "Task created", "task": task})


# ---------------------- GET TASKS --------------------------
@app.route("/tasks", methods=["GET"])
def get_tasks():
    username, role, error = verify_token()
    if error:
        return jsonify({"message": "Invalid token"}), 401

    if role == "admin":
        return jsonify({"tasks": tasks})

    user_tasks = [t for t in tasks if t["owner"] == username]
    return jsonify({"tasks": user_tasks})


# --------------------- UPDATE TASK -------------------------
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    username, role, error = verify_token()
    if error:
        return jsonify({"message": "Invalid token"}), 401

    for task in tasks:
        if task["id"] == task_id:
            if role != "admin" and task["owner"] != username:
                return jsonify({"message": "Not allowed"}), 403

            data = request.get_json()
            task["status"] = data.get("status", task["status"])

            return jsonify({"message": "Task updated", "task": task})

    return jsonify({"message": "Task not found"}), 404


# --------------------- DELETE TASK -------------------------
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    username, role, error = verify_token()
    if error:
        return jsonify({"message": "Invalid token"}), 401

    for task in tasks:
        if task["id"] == task_id:
            if role != "admin" and task["owner"] != username:
                return jsonify({"message": "Not allowed"}), 403

            tasks.remove(task)
            return jsonify({"message": "Task deleted"})

    return jsonify({"message": "Task not found"}), 404


# ------------------------ RUN ------------------------------
if __name__ == "__main__":
    app.run(debug=True)

