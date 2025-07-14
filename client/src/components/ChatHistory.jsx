import "../index.css"; // 👈 create this file for custom styling

export default function ChatHistory({ history }) {
  return (
    <div className="chat-history">
      <h2 className="chat-title">Chat History</h2>
      {history.map((item, i) => (
        <div key={i} className="chat-entry">
          <p><strong>Q:</strong> {item.q}</p>
          <p><strong>A:</strong> {item.a}</p>
        </div>
      ))}
    </div>
  );
}
