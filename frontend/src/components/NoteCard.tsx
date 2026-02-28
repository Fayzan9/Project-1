import "../index.css"

type Note = {
    id: string;
    title: string;
    content: string;
    tags: string[];
    created_at: string;
    updated_at: string;
  };
  
  type NoteCardProps = {
    note: Note;
  };
  
  function NoteCard({ note }: NoteCardProps) {
    return (
      <div className="note-card">
        <h3>{note.title}</h3>
        <p>{note.content}</p>
        <span className="date">
          {new Date(note.created_at).toLocaleString()}
        </span>
  
        {note.tags.length > 0 && (
          <div className="tags">
            {note.tags.map((tag) => (
              <span key={tag} className="tag">
                #{tag}
              </span>
            ))}
          </div>
        )}
      </div>
    );
  }
  
  export default NoteCard;