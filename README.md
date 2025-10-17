# Lemmatica
### Moore's Template Statement

#### 1. FOR:
Social service employees and casual language learners
#### 2. WHO 
Need a simple way to capture and practice real-world phrases.
#### 3. LEMMATICA 
Is a minimalist application
#### 4. THAT 
Allows users to build a personalized knowledge base with built-in recall practice.
##### 5. UNLIKE 
Duolingo or Google Translate,
##### 6. LEMMATICA 
is simple, user-focused, and built to facilitate conversations. Language learners can
log and review words from their daily encounters, while also having access to essential vocabulary terms
in areas like social services and emergency assistance. Inputted words and phrases become a card with
the equivalent translation pulled via API. Users can then study using a recall flashcard technique, and
optionally study with curated “essential vocab” packs designed for immigrant and refugee support.


### Instructions 

#### 1. Clone the Repository

#### 2. Create virtual environment
```python -m venv venv ```
Activate:
mac: 
```source venv/bin/activate```
windows: 
```venv\Scripts```

#### 3. Install Dependencies
```pip install -r requirements.txt```

#### 4. Create a database
Go into the root of the directory in ```cen-project\``` and create a new file, call it "database.sqlite3". We won't have anything in there yet but that's where the setup_db.py file will create tables in, and where we will write to for our database. 

Also I highly recommend installing the plugin "Sqlite Viewer" because it will let you open up our sql database and peak inside of it.

#### 5. Run Application
```flash --app app run``` or ```flask run```
Then visit: Visit: http://127.0.0.1:5000 in your web browser


### File Structure Breakdown 

```flashcards_app/
│
├── app.py # Flask entry point
├── config.py # App configuration (DB URI, secret key, etc.)
├── requirements.txt # Python dependencies
│
├── /app/
│ ├── init.py # App factory, registers blueprints, initializes extensions
│ ├── extensions.py # Shared Flask extensions (db = SQLAlchemy())
│ ├── /models/
│ │ └── orm_objects.py # SQLAlchemy ORM classes (User, Card, Set, CardSet)
│ ├── /scripts/
│ │ └── setup_db.py # Script to initialize database and tables
│ │
│ ├── /main/ # Dashboard and general pages
│ │ ├── init.py
│ │ ├── routes.py
│ │ └── templates/dashboard.html
│ │
│ ├── /auth/ # Authentication (signup/login)
│ │ ├── init.py
│ │ └── routes.py
│ │
│ ├── /cards/ # Flashcard CRUD
│ │ ├── init.py
│ │ └── routes.py
│ │
│ ├── /sets/ # Set CRUD
│ │ ├── init.py
│ │ └── routes.py
│ │
│ └── /practice/ # Practice sessions
│ ├── init.py
│ └── routes.py
│
└── /app/templates/ # Global shared templates
├── base.html # Main layout with header, content blocks
└── layout_header.html # Navigation/header included in base.html```

Blueprints: Each feature (auth, cards, sets, practice, main) is separated into its own module. These are called "blueprints"

Database: Uses SQLAlchemy ORM. Models are in /app/models/orm_objects.py. Tables are created via /app/scripts/setup_db.py. We will write these later when we are ready, once we've designed our ER model.

Templates: Jinja templates are in /app/templates (global) or in blueprint-specific templates/ folders. You can edit these to see changes.
