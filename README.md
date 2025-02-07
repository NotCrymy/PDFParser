# 📄 PDFParser - Open Source PDF Extraction Tool

**PDFParser** is a free and open-source software designed to extract **text** and **images** from PDF files.  
It is built using **Python** and provides multiple export formats (**TXT - PNG**).  
Future updates will include **Improvment of  graphic interface, more export format and multiple export**.

---

## ✨ Features
✔ Extract **text** from PDFs  
✔ Extract **images** from PDFs  
✔ Export results as **TXT or images**  
✔ Handle errors and corrupted PDFs gracefully  
✔ Working with GUI and in command line 

---

## 🚀 Installation
### **Prerequisites**
- **Python 3.8+** installed  
- Install required dependencies :
  ```bash
  pip install -r requirements.txt

---

## 📂 Extract text from a PDF :
  ```bash
  python src/main.py

---

## 📄 Extra note :
Why did I created this tool ?

I developed this tool to reduce the size of PDF files and make them more suitable for use with AI LLM models.

Large PDF documents often contain extraneous formatting, images, and metadata that are unnecessary for AI processing. By extracting and converting them into plain text (TXT),
this tool optimizes the input for AI models, preventing context overflow and improving processing efficiency.

This approach allows AI models to retain more relevant information within their context window, making them more effective at analyzing and understanding large volumes of text.

Eventually you also want them to analyse images so I add that to the tool too
