# database/notes_db.py

import uuid
from datetime import datetime
from database.connection import get_connection


def create_note(title: str, content: str, tags: list[str]):
    conn = get_connection()
    cursor = conn.cursor()

    note_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()

    cursor.execute(
        """
        INSERT INTO notes (id, title, content, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (note_id, title, content, now, now)
    )

    for tag in tags:
        tag_id = str(uuid.uuid4())

        cursor.execute(
            "INSERT OR IGNORE INTO tags (id, name) VALUES (?, ?)",
            (tag_id, tag)
        )

        cursor.execute(
            "SELECT id FROM tags WHERE name = ?",
            (tag,)
        )
        tag_id = cursor.fetchone()["id"]

        cursor.execute(
            "INSERT INTO note_tags (note_id, tag_id) VALUES (?, ?)",
            (note_id, tag_id)
        )

    conn.commit()
    conn.close()

    return note_id


def get_all_notes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            n.id,
            n.title,
            n.content,
            n.created_at,
            n.updated_at,
            t.name AS tag
        FROM notes n
        LEFT JOIN note_tags nt ON n.id = nt.note_id
        LEFT JOIN tags t ON nt.tag_id = t.id
        ORDER BY n.created_at DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    notes_map = {}

    for row in rows:
        note_id = row["id"]

        if note_id not in notes_map:
            notes_map[note_id] = {
                "id": note_id,
                "title": row["title"],
                "content": row["content"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "tags": []
            }

        if row["tag"]:
            notes_map[note_id]["tags"].append(row["tag"])

    return list(notes_map.values())



def attach_tag_to_note(note_id: str, tag_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    # ensure note exists
    cursor.execute("SELECT id FROM notes WHERE id = ?", (note_id,))
    if cursor.fetchone() is None:
        conn.close()
        return "NOTE_NOT_FOUND"

    # ensure tag exists
    cursor.execute("SELECT id FROM tags WHERE id = ?", (tag_id,))
    if cursor.fetchone() is None:
        conn.close()
        return "TAG_NOT_FOUND"

    # prevent duplicate attach
    cursor.execute(
        "SELECT 1 FROM note_tags WHERE note_id = ? AND tag_id = ?",
        (note_id, tag_id)
    )
    if cursor.fetchone():
        conn.close()
        return "ALREADY_ATTACHED"

    # attach tag
    cursor.execute(
        "INSERT INTO note_tags (note_id, tag_id) VALUES (?, ?)",
        (note_id, tag_id)
    )

    conn.commit()
    conn.close()

    return "ATTACHED"




def detach_tag_from_note(note_id: str, tag_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    # check relation exists
    cursor.execute(
        "SELECT 1 FROM note_tags WHERE note_id = ? AND tag_id = ?",
        (note_id, tag_id)
    )
    if cursor.fetchone() is None:
        conn.close()
        return "NOT_ATTACHED"

    # delete relation
    cursor.execute(
        "DELETE FROM note_tags WHERE note_id = ? AND tag_id = ?",
        (note_id, tag_id)
    )

    conn.commit()
    conn.close()
    return "DETACHED"




def get_tags_for_note(note_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    # check note exists
    cursor.execute("SELECT id FROM notes WHERE id = ?", (note_id,))
    if cursor.fetchone() is None:
        conn.close()
        return None  # note not found

    cursor.execute(
        """
        SELECT t.id, t.name
        FROM tags t
        JOIN note_tags nt ON t.id = nt.tag_id
        WHERE nt.note_id = ?
        ORDER BY t.name
        """,
        (note_id,)
    )

    rows = cursor.fetchall()
    conn.close()

    return [
        {"id": row["id"], "name": row["name"]}
        for row in rows
    ]    



def get_notes_for_tag(tag_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    # ensure tag exists
    cursor.execute("SELECT id FROM tags WHERE id = ?", (tag_id,))
    if cursor.fetchone() is None:
        conn.close()
        return None  # tag not found

    cursor.execute(
        """
        SELECT
            n.id,
            n.title,
            n.content,
            n.created_at,
            n.updated_at
        FROM notes n
        JOIN note_tags nt ON n.id = nt.note_id
        WHERE nt.tag_id = ?
        ORDER BY n.created_at DESC
        """,
        (tag_id,)
    )

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row["id"],
            "title": row["title"],
            "content": row["content"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }
        for row in rows
    ]    






def update_note(note_id: str, title: str | None, content: str | None):
    conn = get_connection()
    cursor = conn.cursor()

    # ensure note exists
    cursor.execute("SELECT id FROM notes WHERE id = ?", (note_id,))
    if cursor.fetchone() is None:
        conn.close()
        return None  # note not found

    fields = []
    values = []

    if title is not None:
        fields.append("title = ?")
        values.append(title)

    if content is not None:
        fields.append("content = ?")
        values.append(content)

    # always update timestamp
    fields.append("updated_at = ?")
    values.append(datetime.utcnow().isoformat())

    values.append(note_id)

    query = f"""
        UPDATE notes
        SET {", ".join(fields)}
        WHERE id = ?
    """

    cursor.execute(query, values)
    conn.commit()
    conn.close()

    return True    


from database.connection import get_connection


def delete_note(note_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    # check note exists
    cursor.execute("SELECT id FROM notes WHERE id = ?", (note_id,))
    if cursor.fetchone() is None:
        conn.close()
        return None  # note not found

    # remove relationships first
    cursor.execute(
        "DELETE FROM note_tags WHERE note_id = ?",
        (note_id,)
    )

    # remove the note itself
    cursor.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )

    conn.commit()
    conn.close()
    return True