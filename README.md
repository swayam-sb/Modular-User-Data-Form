# Modular User Data Form

A Django-based **multi-step modular user data collection application** designed to collect and store user information in a structured manner.  

---

## 🚀 Features

- Multi-step form flow:
  - Personal Details
  - Favourite Details
  - Address Details
  - Skills Details
- Modular Django views and templates
- Dark-themed, clean UI using plain CSS
- Data stored using SQLite database
- Fetch page to view all submitted user data

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

Modular-User-Data-Form/
│
├── modular_survey/
├── survey/
│ ├── templates/
│ │ ├── base.html
│ │ ├── form1.html
│ │ ├── form2.html
│ │ ├── form3.html
│ │ ├── form4.html
│ │ ├── thankyou.html
│ │ └── fetch.html
│ │
│ ├── static/
│ │ └── survey/css/dark.css
│ │
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
│
├── manage.py
└── .gitignore
