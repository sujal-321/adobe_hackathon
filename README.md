# adobe_hackathon
# Adobe Hackathon 2025 – Challenge 1A: PDF Outline Extractor

Welcome to the solution for Challenge 1A of the Adobe India Hackathon 2025! This challenge focuses on converting unstructured PDF documents into clean, structured outlines. Our solution is designed to be fast, lightweight, and easy to use — built entirely with Python and Docker.

This tool processes PDF files and extracts:
 The title of the document
Section headings (H1, H2, H3) with their corresponding page numbers

The result is a structured JSON file that summarizes the document's layout, making it easier to read, navigate, and process further.
 Input & Output
 Input:
- PDF files should be placed inside the /input folder.
Output:
- Each input PDF will generate a corresponding .json file inside the /output folder.
Sample output format:
```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "Background", "page": 2 },
    { "level": "H3", "text": "Details", "page": 3 }
  ]
}
```

---

How to Use It

Prerequisites
- Make sure Docker Desktop is installed and running on your machine.
- Place your PDF files in a folder named `input`.

Build the Docker Image
```bash
docker build --platform linux/amd64 -t pdf-outline-extractor .
```

Run the Container
```bash
docker run --rm ^
  -v %cd%\input:/app/input:ro ^
  -v %cd%\output:/app/output ^
  --network none ^
  pdf-outline-extractor
```
> Note: On macOS/Linux, use $(pwd) instead of %cd%

---


Project Structure
```
.
├── Dockerfile              # Container configuration
├── requirements.txt        # Python dependencies
├── challenge_1.py          # Main Python script
├── input/                  # Folder with PDF input files
└── output/                 # Folder where JSON results are saved
```

---

Dependencies
- Python 3.10+
- PyMuPDF (fitz) v1.23.7

Manual installation (outside Docker):
```bash
pip install PyMuPDF==1.23.7
```

