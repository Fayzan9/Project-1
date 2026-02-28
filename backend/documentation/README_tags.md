1. CREATE TAGS

Request JSON
{
  "name": "backend"
}

Success Response (201)
{
  "id": "c3a2d9f4-7c9d-4c92-b2a1-8f19b5e7c011",
  "name": "backend"
}

Error Response (400 – duplicate)
{
  "detail": "Tag already exists"
}


2. GET ALL TAGS

Request
GET /api/tags


Response (200)
[
  {
    "id": "c3a2d9f4-7c9d-4c92-b2a1-8f19b5e7c011",
    "name": "backend"
  },
  {
    "id": "e8a5d2b1-9c44-4c7a-ae12-0d6f1a99a210",
    "name": "study"
  }
]