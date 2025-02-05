# 📄 PDFParser - Open Source PDF Extraction Tool

**PDFParser** is a free and open-source software designed to extract **text** and **images** from PDF files.  
It is built using **Python** and provides multiple export formats (**TXT, CSV, PNG**).  
Future updates will include **a graphical user interface (GUI) and advanced export options**.

---

## ✨ Features
✔ Extract **text** from PDFs  
✔ Extract **images** from PDFs  
✔ Export results as **TXT, CSV, or images**  
✔ Handle errors and corrupted PDFs gracefully  
✔ Fully **command-line based** (GUI planned for future versions)  

---

## 🚀 Installation
### **Prerequisites**
- **Python 3.8+** installed  
- Install required dependencies (coming soon) :
  ```bash
  pip install -r requirements.txt

  
Extract text from a PDF :
python src/main.py

📂 Project Structure

PDFParser/
│── src/                    # Source code
│   ├── main.py             # Main entry point
│   ├── pdf_parser/         # Core logic
│   ├── export_manager.py   # Handles output files
│   ├── import_manager.py   # Handles PDF import
│   ├── error_handler.py    # Manages errors
│
│── examples/               # Example usage files
│   ├── example_usage.py    # Sample script
│   ├── example.pdf         # Example PDF file
│
│── output/                 # Generated output (ignored by Git)
│── tests/                  # Unit tests (to be implemented)
│── .gitignore              # Ignored files
│── README.md               # Project documentation
│── requirements.txt        # Python dependencies
