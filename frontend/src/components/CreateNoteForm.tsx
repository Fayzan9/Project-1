import { useState } from "react"
import { createNote } from "../api/notes.api"
import type { Note } from "../types/note"
import "../index.css"

interface Props {
  onCreated: (note: Note) => void
}

export default function CreateNoteForm({ onCreated }: Props) {
  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")
  const [loading, setLoading] = useState(false)

  const submitHandler = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)

    try {
      const newNote = await createNote(title, content)
      onCreated(newNote)
      setTitle("")
      setContent("")
    } finally {
      setLoading(false)
    }
  }

  return (
    <form onSubmit={submitHandler} className="bg-white p-4 rounded-xl shadow-sm mb-6">
      <input
        className="w-full border rounded-md p-2 mb-3"
        placeholder="Title"
        value={title}
        onChange={e => setTitle(e.target.value)}
        required
      />

      <textarea
        className="w-full border rounded-md p-2 mb-3"
        placeholder="Content"
        value={content}
        onChange={e => setContent(e.target.value)}
        required
      />

      <button
        disabled={loading}
        className="bg-black text-white px-4 py-2 rounded-md hover:bg-gray-800"
      >
        {loading ? "Saving..." : "Create Note"}
      </button>
    </form>
  )
}