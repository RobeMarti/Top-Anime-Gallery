# 🎬Top-Anime-Gallery
An interactive gallery featuring some scenes from my favorite animes, built with Flask.
Each title reveals three scenes with simple animations.

# ⚙️Technologies
- Python
- Flask
- SqlAlchemy
- HTML
- CSS
- JavaScript

# 🚀 Installation and Setup Guide

<b><u>(The commands may be different in your case. In mine, I used python3 and py based on the computer I was working on.)</u></b>

Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

Step 1: Download the Project
Option A: Using Git
```
git clone https://github.com/RobeMarti/Top-Anime-Gallery
cd top-anime-gallery
```

Option B: Download ZIP
- Download the ZIP file from GitHub
- Extract it to your desired location
- Open a terminal in the extracted folder

Step 2: Create a Virtual Environment
Creating a virtual environment is highly recommended to isolate project dependencies.

On Windows:
```
python -m venv venv
venv\Scripts\activate.ps1 
```

On macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```
You should see (venv) at the beginning of your terminal prompt, indicating the virtual environment is active.

Step 3: Install Required Dependencies
With the virtual environment activated, install all necessary packages:
``pip install flask flask-sqlalchemy``

Dependencies included:
- flask - Web framework
- flask-sqlalchemy - SQLAlchemy integration for Flask
- sqlalchemy - ORM for database management (installed automatically with - flask-sqlalchemy)

Step 4: Verify Project Structure
Make sure your project structure looks like this:
```
Top-Anime-Gallery/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html
│   │   └── add_anime.html
│   └── static/
│       ├── CSS/
│       │   ├── gallery.css
│       │   └── add_anime.css
│       ├── JavaScript/
│       │   └── main.js
│       └── public/          (will be created automatically)
├── instance/                 (will be created automatically)
├── main.py
├── create_db.py
└── README.md
```
Step 5: Initialize the Database
Before running the application, you need to create the database and tables:

``python create_db.py`` 
Expected output:
```
Database e tabelle creati correttamente!
Percorso database: sqlite:///anime.db
Tabelle create: ['anime', 'gif']
```

This script will:
- Create the instance/ folder
- Generate the anime.db SQLite database file
- Create the anime and gif tables
