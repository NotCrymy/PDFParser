from pdf_parser.import_manager import ImportManager
from pdf_parser.pdf_parser import PDFParser
from pdf_parser.export_manager import ExportManager
from pdf_parser.error_handler import ErrorHandler

def main():
    print("Welcome to PDFParser! Processing a PDF file...\n")

    # Initialize components
    error_handler = ErrorHandler()
    import_manager = ImportManager()
    export_manager = ExportManager()

    try:
        # Step 1: Import the PDF file
        pdf_file = import_manager.import_file()  # User selects a file via CLI
        print("PDF imported successfully!\n")

        # Step 2: Parse the PDF (text and images)
        pdf_parser = PDFParser(pdf_file)
        text_output = pdf_parser.parse_text()
        image_output = pdf_parser.parse_images()
        print("🔍 Parsing completed!\n")

        # Step 3: Auto-save results
        export_manager.text_outputs.append(text_output)
        export_manager.image_outputs.append(image_output)

        export_manager.export_to_txt("output/text_output.txt")
        export_manager.export_to_csv("output/text_output.csv")
        export_manager.export_images("output/images")

        print("All files have been successfully exported!\n")

    except Exception as e:
        error_handler.handle_error("Main", "main", e)

    # Print any logged errors
    if error_handler.get_errors():
        print("\nErrors encountered:")
        for err in error_handler.get_errors():
            print(f"  - {err}")

if __name__ == "__main__":
    main()