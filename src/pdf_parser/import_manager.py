import os
from pdf_parser.pdf_file import PDFFile

class ImportManager:
    def __init__(self):
        """
        Initializes the ImportManager with no associated PDF file initially.
        """
        self.file = None

    def import_file(self, pdf_path: str = None) -> PDFFile:
        """
        Imports a PDF file by asking the user for a path (if not provided).
        :param pdf_path: Optional, path to the PDF file.
        :return: An instance of the PDFFile class.
        :raises FileNotFoundError: If the file is not found.
        :raises ValueError: If the file is not a valid PDF.
        """
        if not pdf_path:
            pdf_path = self._get_user_input()

        # Verify the file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"Error: The file '{pdf_path}' was not found.")

        # Verify it's a PDF file
        if not pdf_path.lower().endswith(".pdf"):
            raise ValueError("Error: The selected file is not a valid PDF.")

        try:
            # Create PDFFile instance
            self.file = PDFFile(pdf_path)
            self.file.load_file()
            print(f"Successfully imported: {pdf_path}")
            return self.file

        except Exception as e:
            raise Exception(f"Error importing PDF file: {e}")

    def _get_user_input(self) -> str:
        """
        Prompts the user to enter a valid PDF file path.
        :return: The selected file path.
        """
        while True:
            pdf_path = input("Enter the path to the PDF file: ").strip()
            if os.path.exists(pdf_path) and pdf_path.lower().endswith(".pdf"):
                return pdf_path
            else:
                print("Invalid file. Please enter a valid PDF file path.")
