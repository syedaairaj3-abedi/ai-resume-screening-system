import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    text = ""

    pdf_bytes = pdf_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    for page in doc:
        text += page.get_text()

    doc.close()
    pdf_file.seek(0)

    return text
