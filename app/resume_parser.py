def extract_resume_text(pdf_bytes):
    pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_bytes))
    text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    return text
