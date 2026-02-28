1. FOR CREATE NOTE
POST /api/notes

Request JSON
{
  "title": "Meeting Notes",
  "content": "Discuss project timeline and deliverables"
}

Response JSON (201 – Created)
{
  "id": "9f2b1c6e-5d1a-4b92-a3d7-3c0a9f4e8c21",
  "title": "Meeting Notes",
  "content": "Discuss project timeline and deliverables",
  "tags": [],
  "created_at": "2026-02-28T12:45:30.123456",
  "updated_at": "2026-02-28T12:45:30.123456"
}



2. GET ALL Notes
GET /api/notes
Request

❌ No request body
(Optional query params later, but not now)

Response JSON (200 – OK)
[
  {
    "id": "9f2b1c6e-5d1a-4b92-a3d7-3c0a9f4e8c21",
    "title": "Meeting Notes",
    "content": "Discuss project timeline and deliverables",
    "tags": [],
    "created_at": "2026-02-28T12:45:30.123456",
    "updated_at": "2026-02-28T12:45:30.123456"
  },
  {
    "id": "1a7c9d44-8f51-4c0a-b9e1-6f12dbe98210",
    "title": "Study Plan",
    "content": "Revise backend architecture",
    "tags": ["backend", "study"],
    "created_at": "2026-02-28T13:10:05.654321",
    "updated_at": "2026-02-28T13:10:05.654321"
  }
]



