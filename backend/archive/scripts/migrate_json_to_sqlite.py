import json
from pathlib import Path
from database.schema import init_db
from database.connection import get_connection


# Path to old JSON database
JSON_PATH = Path(__file__).parent.parent / "data.json"


def migrate():
    print("🚀 Starting JSON → SQLite migration")

    # 1. Load JSON
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    notes = data.get("notes", [])

    # 2. Ensure tables exist
    init_db()

    conn = get_connection()
    cursor = conn.cursor()

    # 3. Insert notes
    for note in notes:
        cursor.execute(
            """
            INSERT OR IGNORE INTO notes (id, title, content, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                note["id"],
                note["title"],
                note["content"],
                note["created_at"],
                note["updated_at"],
            ),
        )

        for tag in note.get("tags", []):
            # Insert tag
            cursor.execute(
                """
                INSERT OR IGNORE INTO tags (id, name)
                VALUES (?, ?)
                """,
                (tag["id"], tag["name"]),
            )

            # Link note ↔ tag
            cursor.execute(
                """
                INSERT OR IGNORE INTO note_tags (note_id, tag_id)
                VALUES (?, ?)
                """,
                (note["id"], tag["id"]),
            )

    conn.commit()
    conn.close()

    print("✅ Migration completed successfully")


if __name__ == "__main__":
    migrate()