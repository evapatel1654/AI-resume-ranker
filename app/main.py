from fastapi import FastAPI, File, UploadFile
import PyPDF2
from io import BytesIO
from resume_parser import extract_resume_text

app = FastAPI()

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are supported"}
    
    text = extract_resume_text(await file.read())
    
    return {"filename": file.filename, "extracted_text": text[:500]} 
