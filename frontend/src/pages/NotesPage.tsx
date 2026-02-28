import { useEffect, useState } from "react"
import { getAllNotes } from "../api/notes.api"
import type { Note } from "../types/note"
import NotesList from "../components/NotesList"
import CreateNoteForm from "../components/CreateNoteForm"

export default function NotesPage() {
  const [notes, setNotes] = useState<Note[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getAllNotes()
      .then(setNotes)
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Notes App</h1>

      <CreateNoteForm
        onCreated={(note) => setNotes(prev => [note, ...prev])}
      />

      {loading ? (
        <p>Loading...</p>
      ) : (
        <NotesList notes={notes} />
      )}
    </div>
  )
}