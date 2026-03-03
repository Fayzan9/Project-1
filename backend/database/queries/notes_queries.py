# CREATE
CREATE_NOTE_QUERY = """
INSERT INTO notes (id, title, content, created_at, updated_at)
VALUES (?, ?, ?, ?, ?)
"""

# TAGS
INSERT_OR_IGNORE_TAG_QUERY = """
INSERT OR IGNORE INTO tags (id, name) VALUES (?, ?)
"""

SELECT_TAG_ID_BY_NAME = """
SELECT id FROM tags WHERE name = ?
"""

INSERT_NOTE_TAG = """
INSERT INTO note_tags (note_id, tag_id) VALUES (?, ?)
"""

# FETCH
GET_ALL_NOTES_QUERY = """
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
"""

CHECK_NOTE_EXISTS = "SELECT id FROM notes WHERE id = ?"

CHECK_TAG_EXISTS = "SELECT id FROM tags WHERE id = ?"

CHECK_NOTE_TAG_EXISTS = """
SELECT 1 FROM note_tags WHERE note_id = ? AND tag_id = ?
"""

DELETE_NOTE_TAG = """
DELETE FROM note_tags WHERE note_id = ? AND tag_id = ?
"""

GET_TAGS_FOR_NOTE = """
SELECT t.id, t.name
FROM tags t
JOIN note_tags nt ON t.id = nt.tag_id
WHERE nt.note_id = ?
ORDER BY t.name
"""

GET_NOTES_FOR_TAG = """
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
"""

DELETE_NOTE_TAGS = "DELETE FROM note_tags WHERE note_id = ?"

DELETE_NOTE = "DELETE FROM notes WHERE id = ?"