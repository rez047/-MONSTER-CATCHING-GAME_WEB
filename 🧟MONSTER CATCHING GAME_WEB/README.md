# 🧟 Monster Catching Game (Flask)

A web-based monster catching game built with Python Flask.

The application includes:

- User registration
- User login/logout
- Trainer accounts
- Random monster encounters
- Monster catching system
- Monster collection
- Training system
- Monster evolution
- Battles
- SQLite database storage

---

# 🚀 How To Run The Project

## 1. Check Python Installation

Make sure Python is installed.

Run:

```bash
python --version
```

Example:

```
Python 3.x.x
```

Check pip:

```bash
pip --version
```

---

# 2. Open Project Folder

Open a terminal inside the project folder.

Example:

```bash
cd Monster_Catching_Web
```

Your folder should contain:

```
app.py
requirements.txt
templates/
static/
```

---

# 3. Install Required Libraries

Run:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and automatically installs every Python package needed for the project.

---

# 📦 Requirements Explained

## Flask

Installed with:

```
Flask
```

### Purpose

Flask is the web framework used to create the application.

It handles:

- Creating the web server
- URL routes
- Receiving browser requests
- Sending HTML pages
- Connecting frontend pages to Python code


Example:

```python
@app.route("/world")
def world():

    return "Monster Area"
```

When the user visits:

```
/world
```

Flask runs that function.

---

# Flask-SQLAlchemy

Installed with:

```
Flask-SQLAlchemy
```

### Purpose

Flask-SQLAlchemy connects Flask to a database.

It allows Python classes to become database tables.

This project uses it to store:

- Users
- Passwords
- Monsters
- Levels
- XP
- Teams


Example:

```python
class Monster(db.Model):

    name = db.Column(db.String(50))
```

Creates a Monster table in the database.

Without it:

- Data disappears after closing the program

With it:

- Progress is saved

---

# Flask-Login

Installed with:

```
Flask-Login
```

### Purpose

Handles user authentication.

It provides:

- Login sessions
- Logout
- Remembering logged-in users
- Protecting pages


Example:

```python
@login_required
def team():

    return "My Monsters"
```

Only logged-in trainers can open the team page.

---

# Werkzeug

Installed with:

```
Werkzeug
```

### Purpose

Werkzeug is a security library used by Flask.

This project uses it for password encryption.

Instead of saving:

```
mypassword123
```

The database stores a secure hash:

```
pbkdf2:sha256:...
```

Example:

```python
generate_password_hash(password)
```

This protects user accounts.

---

# ▶ Starting The Game

After installing requirements:

Run:

```bash
python app.py
```

You should see:

```
Running on http://127.0.0.1:5000
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 📁 Project Structure

```
Monster_Catching_Web/

│
├── app.py

├── requirements.txt

├── templates/
│   ├── register.html
│   ├── login.html
│   ├── world.html
│   ├── team.html
│   └── battle.html

│
└── static/
    ├── css/
    │   └── style.css
    │
    └── images/
        ├── fire.png
        ├── water.png
        ├── earth.png
        └── air.png
```

---

# 🎮 Gameplay Flow

1. Create a trainer account

2. Login

3. Explore the world

4. Find wild monsters

5. Catch monsters

6. View your team

7. Train monsters

8. Battle

9. Evolve stronger monsters


---

# 🔮 Possible Future Upgrades

- More monster types
- Evolution stages
- Items
- Monster database
- Trading
- Multiplayer battles
- Admin dashboard
- API version
- React frontend

---

# Requirements File

Current:

```
Flask
Flask-SQLAlchemy
Flask-Login
Werkzeug
```

These four packages provide:

- Web server
- Database
- Authentication
- Security