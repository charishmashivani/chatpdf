# ChatPDF

## Table of Contents

- [Overview](#overview)
- [Contents](#contents)
- [Tech-stack](#tech-stack)
- [Setup](#setup)
- [Usage](#usage)
- [Working](#working)

## Overview

I've developed a Python script that extracts text from a PDF file and generates a summary using natural language processing. This project demonstrates my skills in working with PDFs, using NLP libraries, and basic Python programming.

## Contents

1. `specific_content_text.pdf`: Sample PDF containing a short story
2. `summary.py`: Main script for PDF text extraction and summarization

## Tech-stack

- Python 3.x
- PyMuPDF (fitz) for PDF text extraction
- Hugging Face Transformers for text summarization

## Setup

To run this project:

1. Clone this repository
2. Install the required libraries:
   
   ```
   pip install PyMuPDF transformers torch
   ```

## Usage

Run the main script:

```
python summary.py
```

This will process `specific_content_text.pdf` and output a summary to the console.

## Working

The `summary.py` script:
1. Extracts text from the PDF using PyMuPDF
2. Generates a summary using the BART-large-CNN model from Hugging Face Transformers
