# Order Handling System

A simple Flask backend for managing orders with full CRUD operations and action logging.

## Features

- **Add New Order**  
  - Order ID (auto-generated)  
  - Number of items  
  - Delivery date  
  - Sender name  
  - Recipient name  
  - Recipient address  
  - Status (default: “Ongoing”)

- **Edit Orders**  
- **Mark Orders as Delivered**  
- **Delete Orders**  
- **Action Logs**  
  - Tracks Created, Edited, Delivered, Deleted  
  - Records action type, performer, timestamp  
- **Minimal HTML UI**  
  - Orders list view  
  - Order form (new/edit)  
  - Logs list view  
  - Styled with Bootstrap + custom CSS  

## Installation

1. **Clone** this repository or download the ZIP.  
2. **Install dependencies** (requires Python and pip):
   ```bash
   pip install Flask Flask-SQLAlchemy

## Running the App
In your project folder, run:

python app.py
Visit in your browser:

Orders: http://127.0.0.1:5000/orders

Logs: http://127.0.0.1:5000/logs

## Project Structure

order_system/
├── app.py            # Flask routes and app startup
├── config.py         # Database config
├── models.py         # SQLAlchemy models
├── requirements.txt  # pip dependencies
├── README.md         # Project overview & instructions
├── static/
│   └── style.css     # Custom CSS
└── templates/
    ├── base.html
    ├── orders.html
    ├── order_form.html
    └── logs.html