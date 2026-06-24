
Projects:

1. ⚔️ RPG Battle Game
2. 🧟 Monster Catching Game


---

# PART 1 — Understanding The Goal

Before writing code, we decide what we want to build.

A game is made of:

1. Data
2. Rules
3. Interface


Example:

RPG Game:

Data:

```

Hero name
Hero level
Hero health
Hero attack
Enemy health

```

Rules:

```

When player attacks:
Enemy loses health

When XP reaches 100:
Level increases

```

Interface:

```

Buttons
Images
Pages
Forms

```

Python handles the logic.

Flask connects Python to the browser.


---

# PART 2 — Why We Use Flask


## What is Flask?

Flask is a Python web framework.

A framework is a collection of tools that helps us build applications faster.


Without Flask:

Python program:

```

Run
Input
Output
Close

```

It only works in the terminal.


With Flask:

```

Browser
|
|
Flask
|
|
Python Code
|
|
Database

```


The user interacts through a website.


---

# PART 3 — Installing Requirements


We created:

requirements.txt


Inside:

```

Flask
Flask-SQLAlchemy
Flask-Login
Werkzeug

```


Then:

```

pip install -r requirements.txt

```


This means:

"Install every library listed in this file."


---

# PART 4 — Project Structure


We use:

```

Project

app.py

templates/

static/

```


Why?


Because every application has different responsibilities.


---

# app.py


This is the brain.

It contains:

- Flask setup
- Database
- Classes
- Routes
- Game logic


Everything starts here.


When we run:

```

python app.py

```


Python executes this file.


---

# templates Folder


Contains HTML pages.


Example:

```

login.html
battle.html
dashboard.html

````


Why separate HTML?


Because Python should not create webpages manually.


Bad:

```python
return "<h1>Hello</h1>"
````

Good:

```python
return render_template("battle.html")
```

Flask loads the HTML file.

---

# static Folder

Contains files that do not change.

Examples:

```
CSS
Images
Javascript
```

CSS controls appearance.

Images display characters.

Javascript adds interaction.

---

# PART 5 — Creating The Flask Application

We start with:

```python
from flask import Flask


app = Flask(__name__)
```

Explanation:

Import Flask:

"Bring Flask tools into Python"

Create app:

"Create our website"

The app becomes the server.

---

# PART 6 — Database

Problem:

If we store data in variables:

```python
username="John"
```

When the program closes:

Data disappears.

Solution:

Database.

We use:

```
Flask-SQLAlchemy
```

It connects Python with SQLite.

---

# Database Concept

A database contains tables.

Example:

User table:

| id | username | password |
| -- | -------- | -------- |
| 1  | John     | hash     |

Hero table:

| name   | hp  | level |
| ------ | --- | ----- |
| Knight | 150 | 2     |

---

# Creating Models

A model represents data.

Example:

```python
class Hero(db.Model):
```

Means:

"Create a Hero table."

Inside:

```python
hp=db.Column(db.Integer)
```

Means:

Create a number column called hp.

---

# PART 7 — Authentication

Why login?

Because every player needs their own progress.

Without login:

Everyone shares the same hero.

With login:

John has:

```
John's Hero
```

Mary has:

```
Mary's Hero
```

---

# Flask-Login

Handles:

* Login
* Logout
* Sessions

A session remembers:

"This browser belongs to this user."

---

# Password Security

Never save:

```
password123
```

Instead:

```
hash12398asdk
```

Werkzeug creates the hash.

Example:

```python
generate_password_hash(password)
```

---

# PART 8 — Object Oriented Programming

Games naturally use objects.

Real world:

A monster has:

* Name
* HP
* Attack

So we create:

```python
class Monster:
```

Now every monster follows the same structure.

---

# RPG Classes

Hero:

```python
Hero()
```

Enemy:

```python
Enemy()
```

Example:

```python
hero.attack
```

means:

"The hero's attack power"

---

# Monster Game Classes

Monster:

```python
Monster()
```

Contains:

```
name
type
hp
attack
level
xp
```

---

# PART 9 — Routes

Routes connect URLs to Python.

Example:

```python
@app.route("/battle")
```

Means:

When user visits:

```
website.com/battle
```

Run this function.

---

# Common Routes

Register:

```
/
```

Login:

```
/login
```

Dashboard:

```
/dashboard
```

Battle:

```
/battle
```

---

# PART 10 — Forms

HTML sends data:

Example:

```html
<input name="username">
```

Python receives:

```python
request.form["username"]
```

Flow:

User types:

```
John
```

Browser sends:

```
username=John
```

Flask receives it.

---

# PART 11 — RPG Battle Logic

The battle works using rules.

Example:

Hero attacks:

```python
enemy.hp -= hero.attack
```

Meaning:

Enemy health decreases.

---

# Critical Hit

Random numbers create chance.

Example:

```python
random.randint(1,5)
```

If result is 1:

Critical hit.

---

# XP System

After winning:

```python
hero.xp += 50
```

When:

```
XP >=100
```

Level up.

---

# PART 12 — Monster Catching Logic

Finding monsters:

We use random.

Example:

```python
random.choice(monsters)
```

Python chooses one monster.

---

# Catching System

Catch chance:

```python
random.randint()
```

Example:

1-100

If above 40:

Success.

---

# Evolution System

Evolution checks:

```python
if monster.xp >=100
```

Then:

Increase:

```
level
hp
attack
```

---

# PART 13 — The Complete Flow

User opens website:

```
Browser
```

↓

Flask receives request

↓

Route runs

↓

Python logic executes

↓

Database updates

↓

HTML page returned

---

# PART 14 — Skills Learned

After completing these projects students understand:

## Python

* Variables
* Functions
* Classes
* Objects
* Conditions
* Loops
* Random

## Flask

* Routes
* Templates
* Forms
* Sessions

## Database

* Tables
* Models
* Relationships

## Software Design

* Separating files
* Organizing projects
* Building applications

---

# Final Challenge Ideas

Upgrade RPG:

* Add weapons
* Add inventory
* Add magic

Upgrade Monster Game:

* Add 50 monsters
* Add evolution stages
* Add trading

---

# Main Lesson

A game is not just graphics.

A game is:

Data + Rules + Interface

Python creates the rules.

Flask connects them to the web.

Database saves the world.

```

This is structured like a **beginner classroom handout** for a 3–4 hour practical lesson.
```
