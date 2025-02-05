from pdf_parser.pdf_file import PDFFile
from pdf_parser.import_manager import ImportManager
from pdf_parser.pdf_parser import PDFParser
from pdf_parser.export_manager import ExportManager
from pdf_parser.error_handler import ErrorHandler

def main():
    # Initialize components
    error_handler = ErrorHandler()
    import_manager = ImportManager()
    export_manager = ExportManager()

    try:
        # Step 1: Import the PDF file
        pdf_path = "example.pdf"  # Replace with the path to your PDF file
        print(f"Importing file: {pdf_path}")
        pdf_file = import_manager.import_file(pdf_path)

        # Step 2: Parse the PDF (text and images)
        print("Parsing the PDF...")
        pdf_parser = PDFParser(pdf_file)
        text_output = pdf_parser.parse_text()
        image_output = pdf_parser.parse_images()

        # Step 3: Add parsed results to the export manager
        export_manager.text_outputs.append(text_output)
        export_manager.image_outputs.append(image_output)

        # Step 4: Export the results
        print("Exporting results...")
        export_manager.export_to_txt("output/text_output.txt")
        export_manager.export_to_csv("output/text_output.csv")
        export_manager.export_images("output/images")

        print("PDF parsing and export completed successfully!")

    except Exception as e:
        # Handle any errors
        error_handler.handle_error(class_name="Main", method_name="main", error=e)

    # Print logged errors (if any)
    if error_handler.get_errors():
        print("\nLogged Errors:")
        for err in error_handler.get_errors():
            print(err)

if __name__ == "__main__":
    main()
