# # database/adapter.py

# from database.notes_db import create_note, get_all_notes


# def write_db(note_data: dict):
#     """
#     This replaces the old JSON write_db().
#     Same name, new implementation (SQLite).
#     """

#     return create_note(
#         title=note_data["title"],
#         content=note_data["content"],
#         tags=[tag["name"] for tag in note_data.get("tags", [])]
#     )


# def read_db():
#     """
#     This replaces the old JSON read_db().
#     Same name, new implementation (SQLite).
#     """

#     return {
#         "notes": get_all_notes()
#     }