from uuid import uuid4

from database.executor import execute_query
from database.queries.tags_queries import *


class TagsRepository:

    @staticmethod
    def create_tag(name: str):
        existing = execute_query(
            CHECK_TAG_CASE_INSENSITIVE,
            (name,),
            fetchone=True
        )

        if existing:
            return None

        tag_id = str(uuid4())

        execute_query(
            CREATE_TAG_QUERY,
            (tag_id, name),
            commit=True
        )

        return {
            "id": tag_id,
            "name": name
        }

    @staticmethod
    def get_all_tags():
        rows = execute_query(
            GET_ALL_TAGS_QUERY,
            fetchall=True
        )

        return [
            {"id": row["id"], "name": row["name"]}
            for row in rows
        ]