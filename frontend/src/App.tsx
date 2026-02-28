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
    <div className="min-h-screen bg-neutral-50 text-neutral-900 font-sans selection:bg-indigo-100">
      <div className="max-w-5xl mx-auto px-6 py-12">
        {/* Header */}
        <header className="mb-12 flex flex-col items-center text-center">
          <div className="inline-flex items-center justify-center p-3 bg-indigo-600 rounded-2xl shadow-lg shadow-indigo-200 mb-6">
            <svg className="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
            </svg>
          </div>
          <h1 className="text-4xl font-extrabold tracking-tight text-neutral-900 sm:text-5xl mb-3">
            MindNotes
          </h1>
          <p className="text-lg text-neutral-500 max-w-2xl mx-auto">
            Capture your thoughts, ideas, and inspirations in a beautiful, minimalist space.
          </p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12">
          {/* Create Note Section */}
          <section className="lg:col-span-5">
            <div className="sticky top-12 bg-white rounded-3xl shadow-xl shadow-neutral-200/50 border border-neutral-100 p-8">
              <h2 className="text-xl font-bold mb-6 flex items-center gap-2">
                <span className="w-2 h-6 bg-indigo-600 rounded-full"></span>
                Create New Note
              </h2>
              
              <div className="space-y-5">
                <div>
                  <label className="block text-sm font-semibold text-neutral-700 mb-2 ml-1">Title</label>
                  <input
                    type="text"
                    placeholder="E.g., Ideas for next project"
                    className="w-full px-5 py-4 bg-neutral-50 border border-neutral-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all placeholder:text-neutral-400"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                  />
                </div>

                <div>
                  <label className="block text-sm font-semibold text-neutral-700 mb-2 ml-1">Content</label>
                  <textarea
                    placeholder="Type your thoughts here..."
                    rows={6}
                    className="w-full px-5 py-4 bg-neutral-50 border border-neutral-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all placeholder:text-neutral-400 resize-none"
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                  />
                </div>

                <button 
                  className="w-full py-4 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-2xl shadow-lg shadow-indigo-200 transition-all active:scale-[0.98] disabled:opacity-50 disabled:pointer-events-none flex items-center justify-center gap-2"
                  onClick={createNote}
                  disabled={!title.trim() || !content.trim()}
                >
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 4v16m8-8H4" />
                  </svg>
                  Save Note
                </button>
              </div>
            </div>
          </section>

          {/* Notes List Section */}
          <section className="lg:col-span-7">
            <div className="flex items-center justify-between mb-8">
              <h2 className="text-2xl font-bold flex items-center gap-3">
                Your Vault
                <span className="px-2.5 py-0.5 bg-neutral-100 text-neutral-500 text-sm font-medium rounded-full">
                  {notes.length}
                </span>
              </h2>
              <button 
                onClick={fetchNotes}
                className="p-2 text-neutral-400 hover:text-indigo-600 hover:bg-indigo-50 rounded-xl transition-all"
                title="Refresh notes"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
              </button>
            </div>

            {loading ? (
              <div className="flex flex-col items-center justify-center py-20 bg-white rounded-3xl border border-neutral-100 border-dashed">
                <div className="w-10 h-10 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin mb-4"></div>
                <p className="text-neutral-500 font-medium">Syncing with server...</p>
              </div>
            ) : notes.length === 0 ? (
              <div className="flex flex-col items-center justify-center py-20 bg-white rounded-3xl border border-neutral-100 border-dashed text-center px-6">
                <div className="w-16 h-16 bg-neutral-50 rounded-2xl flex items-center justify-center mb-4 text-neutral-300">
                  <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                  </svg>
                </div>
                <h3 className="text-lg font-bold text-neutral-800">No notes yet</h3>
                <p className="text-neutral-500 mt-1">Start by creating your first note on the left.</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
                {notes.map((note) => (
                  <NoteCard key={note.id} note={note} />
                ))}
              </div>
            )}
          </section>
        </div>
      </div>
    </div>
  );
}

export default App;