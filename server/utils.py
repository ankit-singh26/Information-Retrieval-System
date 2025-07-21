import json
import os
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS  # ✅ Fixed import
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

# === CONFIGURATION ===
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
GENERATION_MODEL_NAME = "google/flan-t5-base"
DATA_PATH = os.path.join(os.path.dirname(__file__), "job_skills.json")

# === LOAD JOB SKILLS DATA ===
try:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        JOB_SKILLS_DATA = json.load(f)
except Exception as e:
    print(f"Failed to load job skills: {e}")
    JOB_SKILLS_DATA = []

# === EXTRACT TEXT FROM PDF ===
def extract_text_from_pdf(file_path: str) -> str:
    try:
        doc = fitz.open(file_path)
        return "".join(page.get_text() for page in doc)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

# === BUILD VECTORSTORE IN MEMORY ===
def get_vectorstore(resume_text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=30)
    docs = splitter.create_documents([resume_text], metadatas=[{"source": "resume"}])

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

# === STRICT PROMPT TEMPLATE ===
def build_prompt_template():
    job_skills_str = "\n".join(
        [f"- {job['title']}: {', '.join(job['skills'])}" for job in JOB_SKILLS_DATA]
    )

    few_shots = """
Example 1:
Resume:
Skills: Python, SQL, Data Analysis, Tableau
Question: What job role is suitable for me?
Answer: Data Analyst

Example 2:
Resume:
Skills: React, Node.js, MongoDB, Express.js, Git
Question: What kind of developer role should I apply for?
Answer: Full-Stack Developer

Example 3:
Resume:
Skills: Java, Spring Boot, REST APIs, SQL
Question: What role fits me best?
Answer: Java Developer
"""

    prompt = f"""
You are an expert career advisor.

Given the resume content and a list of job titles with their required skills, your task is to analyze the resume and answer the user's question.

ONLY output **one job title** from the list that best matches the resume's skills. Do not explain. Do not list multiple roles. No bullet points. No extra text.

Here are some examples:

{few_shots}

Now follow the same format for the input below.

Job Titles and Required Skills:
{job_skills_str}

Resume:
{{context}}

Question:
{{question}}
"""
    return PromptTemplate(template=prompt, input_variables=["context", "question"])

# === OPTIONAL OUTPUT CLEANER ===
def clean_output(answer: str) -> str:
    lines = answer.strip().split("\n")
    for line in lines:
        for job in JOB_SKILLS_DATA:
            if job["title"].lower() in line.lower():
                return job["title"]
    return lines[0].strip()

# === CREATE QA CHAIN ===
def create_qa_chain(resume_text: str, generation_model_name=GENERATION_MODEL_NAME):
    vectorstore = get_vectorstore(resume_text)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    gen_pipeline = pipeline(
        "text2text-generation",
        model=generation_model_name,
        max_new_tokens=512,
        do_sample=True,
        top_p=0.9,
        temperature=0.7,
    )
    llm = HuggingFacePipeline(pipeline=gen_pipeline)

    prompt_template = build_prompt_template()
    qa_chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt_template)

    return RetrievalQA(
        combine_documents_chain=qa_chain,
        retriever=retriever,
        input_key="question",
        return_source_documents=False,
    )

# === MAIN TEST ===
if __name__ == "__main__":
    resume_pdf_path = "sample_resume.pdf"  # Change to your actual resume path
    resume_text = extract_text_from_pdf(resume_pdf_path)

    if not resume_text:
        print("No text extracted from resume.")
        exit()

    qa = create_qa_chain(resume_text)
    question = "What job role is suitable for me?"
    raw_answer = qa.run({"question": question})

    print("Raw model output:", raw_answer)
    print("Cleaned answer:", clean_output(raw_answer))
