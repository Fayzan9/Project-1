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


3. GET SPECIFIC NOTE BY ID
API Request & Response

1. Request
GET /api/notes/9f2b1c6e-5d1a-4b92-a3d7-3c0a9f4e8c21

2.Response (200)
{
  "id": "9f2b1c6e-5d1a-4b92-a3d7-3c0a9f4e8c21",
  "title": "Meeting Notes",
  "content": "Discuss project timeline and deliverables",
  "tags": [],
  "created_at": "2026-02-28T12:45:30.123456",
  "updated_at": "2026-02-28T12:45:30.123456"
}


4. UPDATE NOTE BY ID

Request & Response


1.Request JSON
a. ONLY TITLE
{
  "title": "Updated Meeting Notes",
  
}
b. ONLY CONTENT
{
  "content": "Updated timeline and final deliverables"
}
c. BOTH
{
  "title": "Updated Meeting Notes",
  "content": "Updated timeline and final deliverables"
}



2.Response (200)
{
  "id": "9f2b1c6e-5d1a-4b92-a3d7-3c0a9f4e8c21",
  "title": "Updated Meeting Notes",
  "content": "Updated timeline and final deliverables",
  "tags": [],
  "created_at": "2026-02-28T12:45:30.123456",
  "updated_at": "2026-02-28T13:22:10.789123"
}


Error Response (404)
{
  "detail": "Note not found"
}


ATTACH TAG TO NOTE

Request
POST /api/notes/9f2b1c6e-5d1a-4b92-a3d7-3c0a9f4e8c21/tags
{
  "tag_id": "c3a2d9f4-7c9d-4c92-b2a1-8f19b5e7c011"
}


Success Response (200)
{
  "id": "9f2b1c6e-5d1a-4b92-a3d7-3c0a9f4e8c21",
  "title": "Updated Meeting Notes",
  "content": "Updated timeline and final deliverables",
  "tags": [
    {
      "id": "c3a2d9f4-7c9d-4c92-b2a1-8f19b5e7c011",
      "name": "backend"
    }
  ],
  "created_at": "2026-02-28T12:45:30.123456",
  "updated_at": "2026-02-28T14:05:11.442100"
}


REMOVE TAG FROM NOTE

Request
DELETE /api/notes/9f2b1c6e-5d1a-4b92-a3d7-3c0a9f4e8c21/tags/c3a2d9f4-7c9d-4c92-b2a1-8f19b5e7c011
Success Response (200)
{
  "id": "9f2b1c6e-5d1a-4b92-a3d7-3c0a9f4e8c21",
  "title": "Updated Meeting Notes",
  "content": "Updated timeline and final deliverables",
  "tags": [],
  "created_at": "2026-02-28T12:45:30.123456",
  "updated_at": "2026-02-28T14:20:18.998712"
}