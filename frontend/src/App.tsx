import { useEffect, useState } from "react";
import NoteCard from "./components/NoteCard";
import "./index.css"

type Note = {
  id: string;
  title: string;
  content: string;
  tags: string[];
  created_at: string;
  updated_at: string;
};

const API_URL = "http://localhost:8000/api/notes"; // adjust if needed

function App() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [notes, setNotes] = useState<Note[]>([]);
  const [loading, setLoading] = useState(false);

  // 🔹 GET ALL NOTES
  const fetchNotes = async () => {
    setLoading(true);
    try {
      const res = await fetch(API_URL);
      const data = await res.json();
      setNotes(data);
    } catch (error) {
      console.error("Failed to fetch notes", error);
    } finally {
      setLoading(false);
    }
  };

  // 🔹 CREATE NOTE
  const createNote = async () => {
    if (!title.trim() || !content.trim()) return;

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title, content }),
      });

      if (!res.ok) throw new Error("Failed to create note");

      const newNote: Note = await res.json();

      // prepend new note
      setNotes((prev) => [newNote, ...prev]);

      setTitle("");
      setContent("");
    } catch (error) {
      console.error(error);
    }
  };

  // 🔹 Load notes on page load
  useEffect(() => {
    fetchNotes();
  }, []);

  return (
    <>
      {/* CREATE NOTE */}
      <div className="container">
        <input
          type="text"
          placeholder="Note title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <textarea
          placeholder="Type your text here..."
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />

        <button className="cn-btn" onClick={createNote}>
          Create Note
        </button>
      </div>

      {/* NOTES LIST */}
      <div>
        <h1>Get All Notes</h1>

        {loading && <p>Loading notes...</p>}

        <div className="notes-container">
          {!loading && notes.length === 0 ? (
            <p>No notes available</p>
          ) : (
            notes.map((note) => (
              <NoteCard key={note.id} note={note} />
            ))
          )}
        </div>
      </div>
    </>
  );
}

export default App;