import { FilePenLine, Trash2 } from "lucide-react"
import type { Note } from "../types/note"
import { useState } from "react";
import EditNoteModal from "./EditNoteModel";




interface Props {
  note: Note
}



const NoteCard = ({ note }: Props) => {

  const [isEditOpen, setIsEditOpen] = useState(false);
  const [selectedNote, setSelectedNote] = useState<Note | null>(null);

  const handleEditClick = (note: Note) => {
    setSelectedNote(note);
    setIsEditOpen(true);
  };


  return (
    <div className="group relative bg-white p-6 rounded-3xl border border-neutral-100 shadow-sm ">
      <div>
        <div className="flex items-center justify-between">
          <h3 className="text-lg font-bold text-neutral-900 group-hover:text-indigo-600 transition-colors mb-3 pr-4">
            {note.title}
          </h3>
          <div className="flex gap-2">
            <button
              onClick={() => handleEditClick(note)}
              className="bg-indigo-600 text-white p-2 rounded-full hover:bg-indigo-700 transition-colors">
              <FilePenLine className="w-3 h-3" />
            </button>
            <button
              // onClick={() => onDelete()}
              className="bg-red-600 text-white p-2 rounded-full hover:bg-red-700 transition-colors">
              <Trash2 className="w-3 h-3" />
            </button>
          </div>
        </div>
        <div>
          <p className="text-neutral-600 text-sm leading-relaxed line-clamp-4">
            {note.content}
          </p>
        </div>

      </div>

      <div className="mt-6 pt-6 border-t border-neutral-50 flex items-center justify-between">
        <span className="text-[10px] font-bold uppercase tracking-wider text-neutral-400">
          Last updated
        </span>
        <span className="text-xs font-semibold text-neutral-500">
          {new Date(note.updated_at).toLocaleDateString(undefined, { month: 'short', day: 'numeric' })}
        </span>
      </div>

      {/* MODAL */}
      {isEditOpen && selectedNote && (
        <EditNoteModal
          note={selectedNote}
          onClose={() => {
            setIsEditOpen(false);
            setSelectedNote(null);
          }}
        />
      )}

    </div>
  )
}

export default NoteCard