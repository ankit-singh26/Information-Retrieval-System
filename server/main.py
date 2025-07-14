# uvicorn main:app --reload --port 8000
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils import extract_text_from_pdf, create_qa_chain
from model import Question
import os

app = FastAPI()
qa_chain = None
PDF_PATH = "storage/temp.pdf"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    os.makedirs("storage", exist_ok=True)
    with open(PDF_PATH, "wb") as f:
        f.write(contents)

    text = extract_text_from_pdf(PDF_PATH)
    global qa_chain
    qa_chain = create_qa_chain(text)
    return {"message": "PDF processed successfully"}

@app.post("/ask")
async def ask_question(q: Question):
    global qa_chain
    if not qa_chain:
        return {"error": "Please upload a PDF first."}
    answer = qa_chain.run(q.query)
    return {"answer": answer}
