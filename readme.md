# Excel Database Management System

A simple command-line database management system built with Python that stores records in Microsoft Excel files.

The project demonstrates basic CRUD (Create, Read, Update, Delete) concepts using Excel spreadsheets instead of a traditional database.

---

## ✨ Features

- User Authentication
- Registration System
- Excel-based Data Storage
- Create New Databases
- View Database Records
- Modify Existing Records (Work in Progress)
- Command Line Interface

---

## 🛠 Tech Stack

- Python 3
- Pandas
- NumPy
- OpenPyXL

---

## 📂 Project Structure

```
Database_Project/
│
├── main.py             # Main application
├── register.py         # User registration
├── Config.py           # Admin configuration
├── create.py           # Create Excel database
├── modify.py           # Modify records
├── view.py             # View records
├── Users.xlsx          # User database
│
├── username.myext
├── password.myext
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Database_Project.git

cd Database_Project
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

```bash
python register.py
```

or

```bash
python main.py
```

---

## 📦 Dependencies

- Pandas
- NumPy
- OpenPyXL

---

## ⚠️ Notes

This project currently uses absolute file paths inside several Python files.

Example:

```python
/home/username/Desktop/.../Users.xlsx
```

These paths should be changed to relative paths before sharing or deploying the project.

Example:

```python
Users.xlsx
```

or

```python
data/Users.xlsx
```

---

## 🚧 Future Improvements

- Complete Modify Function
- Complete View Function
- Delete Records
- Search Records
- Better Input Validation
- Password Encryption
- SQLite/MySQL Support
- GUI Version (Tkinter/PyQt)
- Export CSV

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shis Maheta**

Python Developer | AI Developer | Full Stack Developer

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
