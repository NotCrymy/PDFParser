import os
from pdf_parser.import_manager import ImportManager
from pdf_parser.pdf_parser import PDFParser
from pdf_parser.export_manager import ExportManager
from pdf_parser.error_handler import ErrorHandler
from gui.pdf_parser_app import PDFParserApp

"""
===================================================
    PDFParser - Main Entry Point
===================================================

This script serves as the main entry point for the PDFParser application.
It initializes the graphical user interface (GUI) and provides a command-line
alternative for parsing and exporting PDF content.

Features:
- Imports a PDF file and extracts text and images.
- Exports extracted data as TXT and PNG files.
- Handles errors and logs them if encountered.
- Launches the graphical interface for user interaction.

Usage:
- Run this script to launch the application:
    python main.py
-- You may only want to run it in command line, in this case call main() in the "__name__" var --

Dependencies:
- Ensure all required modules are installed using:
    pip install -r requirements.txt

Author: Clement
Date project started: 06/02/2025
===================================================
"""

def main():
    print("Starting PDF parsing...")

    # Initialize error handler
    error_handler = ErrorHandler()

    try:
        # Ask the user for a file path
        pdf_path = input("Enter the path to the PDF file: ").strip()

        # Import PDF
        import_manager = ImportManager()
        pdf_file = import_manager.import_file(pdf_path)
        print(f"PDF '{pdf_path}' successfully imported.")

        # Parse PDF
        pdf_parser = PDFParser(pdf_file)
        text_output = pdf_parser.parse_text()
        image_output = pdf_parser.parse_images()
        print("PDF parsing completed.")

        # Export results
        export_manager = ExportManager()  # Purge output once here
        export_manager.text_outputs.append(text_output)
        export_manager.image_outputs.append(image_output)

        print(f"Exporting files to: {os.path.abspath('output/')}")
        export_manager.export_to_txt("output/text_output.txt")
        export_manager.export_images("output/images")

        print("Export completed. Check the 'output/' directory.")

    except Exception as e:
        error_handler.handle_error("Main", "main", e)

    # Display any logged errors
    if error_handler.get_errors():
        print("\nErrors encountered:")
        for err in error_handler.get_errors():
            print(f"  - {err}")

if __name__ == "__main__":
    app = PDFParserApp()
    app.run()