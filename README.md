# ChatPDF

## Project Overview

I've developed a Python script that extracts text from a PDF file and generates a summary using natural language processing. This project demonstrates my skills in working with PDFs, using NLP libraries, and basic Python programming.

## Repository Contents

1. `specific_content_text.pdf`: Sample PDF containing a short story
2. `summary.py`: Main script for PDF text extraction and summarization

## Tech Stack

- Python 3.x
- PyMuPDF (fitz) for PDF text extraction
- Hugging Face Transformers for text summarization

## Setup and Installation

To run this project:

1. Clone this repository
2. Install the required libraries:
   
   ```
   pip install PyMuPDF transformers torch
   ```

## How to Use

Run the main script:

```
python summary.py
```

This will process `specific_content_text.pdf` and output a summary to the console.

## How It Works

The `summary.py` script:
1. Extracts text from the PDF using PyMuPDF
2. Generates a summary using the BART-large-CNN model from Hugging Face Transformers

## Feedback and Contributions

I'm always looking to improve! If you have any suggestions or feedback, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
