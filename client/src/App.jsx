import { useState } from "react";
import axios from "axios";
import ChatHistory from "./components/ChatHistory";
import "./index.css"; // 👈 custom CSS here

const API = "http://localhost:8000";

export default function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [history, setHistory] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [loadingAnswer, setLoadingAnswer] = useState(false);

  const uploadFile = async () => {
    if (!file) {
      alert("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setUploading(true);
      const res = await axios.post(`${API}/upload`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      alert("PDF uploaded and processed.");
    } catch (err) {
      console.error("Upload failed:", err);
      alert("Failed to upload PDF.");
    } finally {
      setUploading(false);
    }
  };

  const askQuestion = async () => {
    if (!question.trim()) return;

    try {
      setLoadingAnswer(true);
      const res = await axios.post(`${API}/ask`, { query: question });
      setAnswer(res.data.answer);
      setHistory([{ q: question, a: res.data.answer }, ...history]);
      setQuestion("");
    } catch (err) {
      console.error("Failed to get answer:", err);
      alert("Failed to get answer.");
    } finally {
      setLoadingAnswer(false);
    }
  };

  return (
    <div className="container">
      <h1 className="title">PDF Q&A App</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadFile} className="btn btn-blue" disabled={uploading}>
        {uploading ? "Uploading..." : "Upload PDF"}
      </button>

      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask something..."
        className="text-input"
      />
      <button onClick={askQuestion} className="btn btn-green" disabled={loadingAnswer}>
        {loadingAnswer ? "Processing..." : "Ask"}
      </button>

      {loadingAnswer && <p className="loading-text">Thinking...</p>}

      {answer && !loadingAnswer && (
        <div className="answer-box">
          <strong>Answer:</strong> {answer}
        </div>
      )}

      <ChatHistory history={history} />
    </div>
  );
}
