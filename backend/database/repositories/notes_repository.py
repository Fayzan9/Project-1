import uuid
from datetime import datetime

from database.executor import execute_query
from database.queries.notes_queries import *


class NotesRepository:

    @staticmethod
    def create_note(title: str, content: str, tags: list[str]):
        note_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()

        execute_query(
            CREATE_NOTE_QUERY,
            (note_id, title, content, now, now),
            commit=True
        )

        for tag in tags:
            tag_id = str(uuid.uuid4())

            execute_query(
                INSERT_OR_IGNORE_TAG_QUERY,
                (tag_id, tag),
                commit=True
            )

            tag_row = execute_query(
                SELECT_TAG_ID_BY_NAME,
                (tag,),
                fetchone=True
            )

            tag_id = tag_row["id"]

            execute_query(
                INSERT_NOTE_TAG,
                (note_id, tag_id),
                commit=True
            )

        return note_id

    @staticmethod
    def get_all_notes():
        rows = execute_query(
            GET_ALL_NOTES_QUERY,
            fetchall=True
        )

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

    @staticmethod
    def delete_note(note_id: str):
        note = execute_query(
            CHECK_NOTE_EXISTS,
            (note_id,),
            fetchone=True
        )

        if not note:
            return None

        execute_query(DELETE_NOTE_TAGS, (note_id,), commit=True)
        execute_query(DELETE_NOTE, (note_id,), commit=True)

        return True