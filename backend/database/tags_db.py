from uuid import uuid4
from database.connection import get_connection


def create_tag(name: str):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM tags WHERE LOWER(name) = LOWER(?)",
            (name,)
        )
        if cursor.fetchone():
            return None

        tag_id = str(uuid4())
        cursor.execute(
            "INSERT INTO tags (id, name) VALUES (?, ?)",
            (tag_id, name)
        )
        conn.commit()

        return {"id": tag_id, "name": name}
    finally:
        conn.close()


def get_all_tags():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM tags ORDER BY name")
        rows = cursor.fetchall()

        return [
            {"id": row["id"], "name": row["name"]}
            for row in rows
        ]
    finally:
        conn.close()