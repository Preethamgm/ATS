# 📝 Applicant Tracking System (ATS)

A simple **Applicant Tracking System (ATS)** built with **FastAPI** (Python) for the backend and **React** (JavaScript) for the frontend. It allows employers to post jobs and applicants to apply.

---

## 📌 Features
✅ Job Posting Management (Create, List, View Jobs)  
✅ Applicant Management (Register, View Applicants)  
✅ Job Application Tracking (Apply, View Applications)  
✅ Authentication (JWT-based Login/Signup for Applicants)  
✅ API Documentation (FastAPI's interactive UI at `/docs`)  

---

## 🏗 Tech Stack
**Backend (FastAPI, Python)**
- FastAPI (API Framework)
- PostgreSQL (Database)
- Alembic (Migrations)
- SQLAlchemy (ORM)
- JWT (Authentication)
- Pydantic (Data Validation)

**Frontend (React, JavaScript)**
- React (UI Framework)
- React Router (Navigation)
- Axios (API Requests)
- Bootstrap/Material-UI (Styling)

---

## 🚀 Getting Started

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/ats-project.git
cd ats-project
```

### **2️⃣ Backend Setup**
1. Navigate to the `backend/` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up `.env` file with the database connection:
   ```bash
   cp .env.example .env
   ```
5. Run database migrations:
   ```bash
   alembic upgrade head
   ```
6. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
7. Open API Docs in your browser:
   ```
   http://localhost:8000/docs
   ```

---

### **3️⃣ Frontend Setup**
1. Navigate to the `frontend/` directory:
   ```bash
   cd ../frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```
4. Open the application in your browser:
   ```
   http://localhost:3000
   ```

---

## 🛠 API Endpoints

| Method | Endpoint            | Description              |
|--------|---------------------|--------------------------|
| GET    | `/jobs/`            | List all job postings   |
| POST   | `/jobs/`            | Create a new job        |
| GET    | `/jobs/{job_id}`    | Get job details         |
| POST   | `/applicants/`      | Register a new applicant |
| GET    | `/applicants/`      | List all applicants     |
| GET    | `/applicants/{id}`  | Get applicant details   |
| POST   | `/applications/`    | Apply for a job         |
| GET    | `/applications/`    | List all applications   |

---

## 🔐 Authentication
- Users can **register** (`POST /applicants/`) and **login** (`POST /auth/token`).
- JWT Tokens are required for protected endpoints.

---

## 🏗 Database Migrations
If you modify `models.py`, create a new migration:
```bash
alembic revision --autogenerate -m "Describe the change"
alembic upgrade head
```

---

## 🛠 Deployment
### **Backend Deployment**
- Deploy to **Heroku, Render, or DigitalOcean**.
- Use **Docker** to containerize the app:
  ```bash
  docker build -t ats-backend .
  docker run -p 8000:8000 ats-backend
  ```

### **Frontend Deployment**
- Deploy to **Vercel or Netlify**.
- Run:
  ```bash
  npm run build
  ```

---

## 📜 License
This project is **open-source** and free to use.

---

## 📢 Contributing
Want to improve this project? Feel free to submit a PR!

🚀 Happy Coding!

