import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

from transformers import pipeline

def summarize_text(text, model_name="facebook/bart-large-cnn"):
    summarizer = pipeline("summarization", model=model_name)
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

pdf_path = "specific_content_text.pdf"
text = extract_text_from_pdf(pdf_path)
summary = summarize_text(text)
print(summary)
