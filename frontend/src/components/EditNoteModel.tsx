interface Props {
  note: Note | null;
  onClose: () => void;
}

const EditNoteModal = ({ note, onClose }: Props) => {
  if (!note) return null;

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-xl w-96">
        <h2 className="text-lg font-bold mb-4">Edit Note</h2>

        <input
          defaultValue={note.title}
          className="w-full border p-2 mb-3"
        />

        <textarea
          defaultValue={note.content}
          className="w-full border p-2 mb-3"
        />

        <button
          onClick={onClose}
          className="bg-indigo-600 text-white px-4 py-2 rounded"
        >
          Close
        </button>
      </div>
    </div>
  );
};

export default EditNoteModal;