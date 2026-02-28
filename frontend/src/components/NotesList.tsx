import type { Note } from "../types/note"
import NoteCard from "./NoteCard"

interface Props {
  notes: Note[]
}

export default function NotesList({ notes }: Props) {
  if (!notes.length) {
    return <p className="text-gray-500">No notes found.</p>
  }

  return (
    <div className="grid gap-4 md:grid-cols-2">
      {notes.map(note => (
        <NoteCard key={note.id} note={note} />
      ))}
    <h1 className="">hi amin</h1>

    </div>
    
  )
}