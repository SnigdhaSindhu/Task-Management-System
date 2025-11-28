📘 Task Management System — Full Stack Project

Project Title: Task Management Web Application with Authentication & Role-Based Access

📝 Overview

This is a full-stack Task Management System that provides secure user authentication, task operations (CRUD), and role-based access control.
The system allows users to register, log in, and manage their tasks through an intuitive dashboard.

There are two roles:

Admin – can view and manage all tasks and users

Normal User – can manage only their own tasks

🔑 Key Features
🔐 Authentication

User Registration

User Login

JWT-based secure authentication

Protected routes

🧑‍🤝‍🧑 Role-Based Access
Feature	User	Admin
Create Task	✔	✔
View Tasks	Own Only	All Tasks
Update Task	✔	✔
Delete Task	Own Only	All Tasks
📝 Task Features

Add New Task

Edit / Update Task

Delete Task

View task owner (Admin only)

Status options: Pending / In Progress / Completed

🎨 UI Features

Modern Login & Register screens

Dashboard with task cards

Responsive layout

Action icons for edit/delete

Navbar with logout

🧰 Tech Stack
Frontend

React.js

Axios

React Router

Custom CSS / Components

Backend

Python

Flask

Flask-CORS

PyJWT

📂 Folder Structure
Task-Management-System/
│
├── backend/
│   ├── app.py
│   ├── venv/
│   └── (other backend files)
│
└── frontend/
    ├── src/
    │   ├── App.js
    │   ├── App.css
    │   ├── pages/
    │   │   ├── Login.js
    │   │   ├── Register.js
    │   │   └── Dashboard.js
    │   └── components/
    └── package.json

🚀 Setup Instructions
1️⃣ Backend Setup (Flask)

Open terminal:

cd backend
python -m venv venv
.\venv\Scripts\activate
pip install flask flask-cors pyjwt
python app.py


Backend runs on:
👉 http://127.0.0.1:5000

2️⃣ Frontend Setup (React)

Open another terminal:

cd frontend
npm install
npm start


Frontend runs on:
👉 http://localhost:3000

🔗 API Endpoints
Route	Method	Description
/register	POST	Register a new user
/login	POST	Login & receive JWT
/tasks	GET	Fetch tasks
/tasks	POST	Create new task
/tasks/<id>	PUT	Update task
/tasks/<id>	DELETE	Delete task
🧭 How to Use the Application

Register as User or Admin

Login

Access dashboard

Create tasks

Update task status

Delete tasks

Admin can view all tasks

Logout

✅ Conclusion

The Task Management System showcases:

Secure JWT authentication

Proper role-based access

Full CRUD functionality

Clean UI and responsive design

Frontend–Backend integration

This project is well-suited for academic submission, internships, and portfolio use.

👤 Submitted By

Snigdha Sindhu
Task Management System – Full Stack Projec
