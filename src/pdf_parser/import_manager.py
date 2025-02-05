from pdf_parser.pdf_file import PDFFile

class ImportManager:
    def __init__(self):
        """
        Initializes the ImportManager with no associated PDF file initially.
        """
        self.file = None

    def import_file(self, pdf_path: str) -> PDFFile:
        """
        Imports a PDF file by creating a PDFFile object and validating it.
        :param pdf_path: Path to the PDF file to be imported.
        :return: An instance of the PDFFile class.
        :raises FileNotFoundError: If the file is not found.
        :raises ValueError: If the file is not a valid PDF.
        """
        self.file = PDFFile(pdf_path)
        self.file.load_file()
        if not self.file.validate_file():
            raise ValueError(f"The file at '{pdf_path}' is not a valid PDF.")
        return self.file

    def validate_file(self) -> bool:
        """
        Validates the associated PDF file.
        :return: True if the file is valid, False otherwise.
        :raises ValueError: If no file is loaded.
        """
        if not self.file:
            raise ValueError("No file has been imported.")
        return self.file.validate_file()

    def report_error(self, error: str) -> None:
        """
        Reports an error encountered during the import process.
        :param error: Description of the error to be reported.
        """
        # For now, just print the error. This can be extended to log errors.
        print(f"ImportManager Error: {error}")
