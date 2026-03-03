CREATE_TAG_QUERY = """
INSERT INTO tags (id, name) VALUES (?, ?)
"""

CHECK_TAG_CASE_INSENSITIVE = """
SELECT id FROM tags WHERE LOWER(name) = LOWER(?)
"""

GET_ALL_TAGS_QUERY = """
SELECT id, name FROM tags ORDER BY name
"""