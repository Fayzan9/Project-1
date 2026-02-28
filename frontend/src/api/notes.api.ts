import type { Note } from "../types/note"
const BASE_URL = "/api/notes"

export const getAllNotes = async (): Promise<Note[]> => {
  const res = await fetch(BASE_URL)
  if (!res.ok) throw new Error("Failed to fetch notes")
  return res.json()
}

export const createNote = async (
  title: string,
  content: string
): Promise<Note> => {
  const res = await fetch(BASE_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, content })
  })

  if (!res.ok) throw new Error("Failed to create note")
  return res.json()
}