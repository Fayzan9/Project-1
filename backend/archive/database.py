import json
import os
from typing import Dict, Any

DB_FILE = "data.json"


def init_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump(
                {
                    "notes": [],
                    "tags": []
                },
                f,
                indent=4
            )


def read_db() -> Dict[str, Any]:
    with open(DB_FILE, "r") as f:
        return json.load(f)


def write_db(data: Dict[str, Any]):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)