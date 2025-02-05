"""
This file is an example of usage of the PDF parser.

It demonstrates how to:
1. Import a PDF file.
2. Parse the PDF to extract text and images.
3. Export the extracted content to TXT, CSV, and image files.

To run this example, make sure you have a valid PDF file named 'example.pdf'
inside the 'examples/' directory.

Usage:
    python examples/example_usage.py
"""

import os
import sys

# Add 'src/' to sys.path to allow imports from the pdf_parser module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from pdf_parser.import_manager import ImportManager
from pdf_parser.pdf_parser import PDFParser
from pdf_parser.export_manager import ExportManager
from pdf_parser.error_handler import ErrorHandler

def run_example():
    print("Starting PDFParser example...")

    # Get the absolute path of example.pdf inside the examples/ folder
    example_pdf_path = os.path.join(os.path.dirname(__file__), "example.pdf")

    # Check if the file exists before proceeding
    if not os.path.exists(example_pdf_path):
        print(f"Error: The file '{example_pdf_path}' was not found.")
        return

    # Initialize error handling
    error_handler = ErrorHandler()

    try:
        # Import PDF
        import_manager = ImportManager()
        pdf_file = import_manager.import_file(example_pdf_path)
        print(f"PDF '{example_pdf_path}' successfully imported.")

        # Parse PDF
        pdf_parser = PDFParser(pdf_file)
        text_output = pdf_parser.parse_text()
        image_output = pdf_parser.parse_images()
        print("PDF parsing completed.")

        # Export results
        output_dir = os.path.join(os.path.dirname(__file__), "output")
        export_manager = ExportManager()
        export_manager.text_outputs.append(text_output)
        export_manager.image_outputs.append(image_output)

        export_manager.export_to_txt(os.path.join(output_dir, "text_output.txt"))
        export_manager.export_to_csv(os.path.join(output_dir, "text_output.csv"))
        export_manager.export_images(os.path.join(output_dir, "images"))

        print(f"\nExport completed. Check the '{output_dir}/' directory.")

    except Exception as e:
        error_handler.handle_error("Example", "run_example", e)

    # Display any logged errors
    if error_handler.get_errors():
        print("\nErrors encountered:")
        for err in error_handler.get_errors():
            print(f"  - {err}")

if __name__ == "__main__":
    run_example()