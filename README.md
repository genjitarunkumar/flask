# Flask Development 🚀

A beginner-friendly Flask development repository containing step-by-step examples for learning Flask, Jinja2 templates, Static Files, SQLAlchemy, Blueprints, Authentication, CRUD operations, File Uploads, and more.

This repository is designed for students and developers who want to master Flask from scratch and build production-ready web applications.

---

## 📁 Project Structure

```
Flask-Development/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   ├── forms/
│   ├── utils/
│   └── __init__.py
│
├── uploads/
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

---

# 🛠 Prerequisites

- Python 3.11+
- Git
- VS Code (Recommended)

Check your Python version

```bash
python --version
```

or

```bash
python3 --version
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/Gagan47raj/Flask-Development.git
```

Move inside the project

```bash
cd Flask-Development
```

---

# 🐍 Create Virtual Environment

## Windows

```bash
python -m venv venv
```

Activate

### Command Prompt

```cmd
venv\Scripts\activate
```

### PowerShell

```powershell
venv\Scripts\Activate.ps1
```

---

## Linux / macOS

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

Upgrade pip

```bash
python -m pip install --upgrade pip
```

Install required packages

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Flask Application

Run the application

```bash
python run.py
```

or

```bash
flask run
```

Application will start on

```
http://127.0.0.1:5000
```

---

# 🔄 Deactivate Virtual Environment

```bash
deactivate
```

---

# 📌 Install New Package

```bash
pip install package_name
```

Update requirements

```bash
pip freeze > requirements.txt
```

---

# 🗃 Database Setup

If using Flask SQLAlchemy

Initialize database

```python
from app.models import db

db.create_all()
```

Or using Flask Shell

```bash
flask shell
```

```python
from app.models import db
db.create_all()
```

---

# 📂 Environment Variables (Optional)

Create a `.env`

```
SECRET_KEY=your-secret-key
FLASK_ENV=development
FLASK_DEBUG=True
```

Install dotenv

```bash
pip install python-dotenv
```

---

# 📚 Topics will be Covered

- Flask Introduction
- Routing
- URL Parameters
- HTTP Methods
- Templates (Jinja2)
- Template Inheritance
- Static Files
- Forms
- WTForms
- Flash Messages
- Sessions
- Cookies
- Blueprints
- SQLAlchemy ORM
- CRUD Operations
- Authentication
- File Upload
- Configuration
- Error Handling
- Pagination
- Flask CLI
- REST API Basics

---

# 💻 Common Commands

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```cmd
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install requirements

```bash
pip install -r requirements.txt
```

Run application

```bash
python run.py
```

Deactivate

```bash
deactivate
```

---

# 📦 Generate requirements.txt

```bash
pip freeze > requirements.txt
```

Install from requirements

```bash
pip install -r requirements.txt
```

---

# 🔍 Verify Installation

```bash
python
```

```python
import flask
print(flask.__version__)
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# ⭐ Support

If this repository helped you learn Flask, consider giving it a ⭐ on GitHub.

---

# 👨‍💻 Author

**Gagan Rajput**

GitHub:
https://github.com/Gagan47raj

Happy Coding! 🚀
