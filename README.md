# 📦 Delivery-Boy-Management-System  

The **Delivery-Boy-Management-System** is a **Django-based web application** designed to help vendors and franchise owners manage delivery operations efficiently.  
It allows tracking delivery boys, managing vendors, monitoring deliveries, and generating reports.  

---

## 📁 Folder Structure  

delivery-boy-management-system/
 
├── manage.py # Django management script
 
├── db.sqlite3 # SQLite database (for development/testing)
 
├── project/ # Main Django project settings
 
├── templates/ # HTML templates
 
├── vendor/ # Vendor app
 
├── owner/ # Owner app

└── README.md # Documentation

---

## 🚀 How to Run Locally  

1. Clone the repository:  
```bash
git clone https://github.com/worthyapple/Delivery-Boy-Management-System.git
cd Delivery-Boy-Management-System
```
2.Create a virtual environment and activate it (recommended):
```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```
3.Install dependencies:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

4.Run the development server:
```bash
python manage.py runserver
```
5.Open in your browser:
```bash
http://127.0.0.1:8000/
```

---
## 📊 Features

🏢 Vendor Management – add, edit, and view vendors

🚚 Delivery Boy Management – track delivery boys and assign tasks

📑 Delivery Reports – generate reports for deliveries and earnings

🔐 Authentication – owner and vendor login system

🖥️ Admin Panel – manage all entities via Django admin

## 📌 Technologies Used

- Python 3 – backend logic

- Django – web framework

- SQLite – default database

- HTML/CSS – frontend templates

## 📖 About

The Delivery-Boy-Management-System helps streamline delivery operations for vendors and franchise owners by providing easy tracking, reporting, and management of delivery personnel.

It’s ideal for small-to-medium businesses that want a lightweight, web-based system for managing deliveries and vendor operations.

