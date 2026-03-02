JSON → SQLite (Step-by-Step)

This document explains how and why this project was migrated from a JSON file–based database to a SQLite relational database.


JSON → SQLite (Step-by-Step)

This document explains how and why this project was migrated from a JSON file–based database to a SQLite relational database.

YOU CAN SEE FILE(data.json) IN ARCHIVE FOLDER


2️⃣ Why We Migrated to SQLite

We migrated to SQLite because:

it supports relations (many-to-many)

it is file-based (no server setup)

it is production-ready

it is easy to ship with applications

it teaches real SQL concepts

SQLite gave us:

notes table

tags table

note_tags junction table


TABELS CREATED IN SCHEMA FILE


4️⃣ Creating the SQLite Database
File used
backend/database/schema.py
Initialization function
def init_db():
    # creates tables if they do not exist
When it runs

The database is initialized automatically when the app starts:

@app.on_event("startup")
def startup():
    init_db()
5️⃣ One-Time Migration Script

To move existing JSON data into SQLite, we wrote a one-time script.

File
backend/scripts/migrate_json_to_sqlite.py
What the script does

Reads old data.json

Inserts notes into notes

Inserts tags into tags

Creates relationships in note_tags

Commits everything into SQLite

▶️ Running the migration

From the backend/ directory:

python -m scripts.migrate_json_to_sqlite

Expected output:

🚀 Starting JSON → SQLite migration
✅ Migration completed successfully

⚠️ Important:
This script is meant to run only once.

After migration:

SQLite becomes the source of truth

JSON is no longer used at runtime

6️⃣ Refactoring the Application Code

After migration, we removed all JSON logic from runtime code.

What changed
Old (JSON)	New (SQLite)
read_db()	SQL SELECT
write_db()	SQL INSERT / UPDATE / DELETE
in-memory mutation	persistent DB operations
single file	normalized tables
New structure
database/
├── connection.py   # SQLite connection
├── schema.py       # table creation
├── notes_db.py     # SQL for notes
└── tags_db.py      # SQL for tags

APIs now call database functions, not JSON helpers.

7️⃣ Archiving the Old JSON Implementation

Instead of deleting JSON code, we archived it for reference.

Location
backend/archive/json_db/
├── README.md
├── database.py
└── data.json
Why archive?

helps others understand the evolution

useful for learning

preserves migration context

Safety measure

The archive/ folder does not contain __init__.py,
so Python cannot import it accidentally.

8️⃣ Setting Up SQLite on a New Machine
Prerequisites

Python 3.10+

Virtual environment activated

Steps
cd backend
python -m venv .venv
.venv/scripts/activate   # Windows
pip install -r requirements.txt
Run the app
uvicorn main:app --reload
What happens automatically

SQLite database file is created (app.db)

Tables are initialized

App is ready to use

9️⃣ How Data Is Used Now

All reads → SQL SELECT

All writes → SQL INSERT / UPDATE / DELETE

Relationships → note_tags

No JSON file is used at runtime

SQLite is now the single source of truth.

10️⃣ Key Learnings from This Migration

This migration demonstrates:

how to evolve a project safely

how to migrate data without losing it

how to separate API and DB layers

how relational databases solve real problems

how to archive legacy systems correctly