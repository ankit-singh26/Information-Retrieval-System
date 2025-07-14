# 📄 PDF Q&A Web App

A free, full-stack Q&A application that allows users to upload a PDF (like a resume) and ask natural language questions based on its content. Built using **React.js** (frontend) and **FastAPI** (backend), and powered by **LangChain** with **local or HuggingFace LLMs**.

---

## 🚀 Features

- Upload and parse any PDF document
- Ask questions based on the content of the uploaded file
- View chat history of previous questions and answers
- Styled with responsive custom CSS
- Easily extensible and free to deploy

---

## 🖼️ Demo

Coming soon!

---

## 🛠️ Tech Stack

| Layer        | Technology          |
|--------------|---------------------|
| Frontend     | React.js, Axios, Vite |
| Backend      | FastAPI, LangChain, PyMuPDF |
| LLM Provider | HuggingFace Hub (or local) |
| Vector Store | FAISS |
| Styling      | Custom CSS |

---

## 📁 Project Structure

Information-Retrieval-System/
├── client/ # React frontend
│ ├── src/
│ │ ├── App.jsx
│ │ ├── index.css
│ │ └── components/
│ │ └── ChatHistory.jsx
│ └── package.json
├── server/ # FastAPI backend
│ ├── app.py
│ ├── utils.py
│ ├── model.py
│ └── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### Backend (FastAPI)
```bash
cd server
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
Frontend (React)
bash
Copy
Edit
cd client
npm install
npm run dev
Open: http://localhost:5173

🌟 Future Ideas
Chat-like interface with streaming output

PDF summary view

Multi-file support

Role recommendation AI for resumes

🤝 Contributions
Feel free to fork and improve the app!

📄 License
MIT License

yaml
Copy
Edit

---

Let me know if you'd like:
- A deploy guide (Vercel + Render)
- A Python `requirements.txt`
- To convert this into a Streamlit app instead of React

Would you like me to generate the `utils.py` and `model.py` content as well?