import os
import fitz

class PDFFile:
    def __init__(self, path: str):
        """
        Initializes a PDFFile object with a file path.
        :param path: Path to the PDF file.
        """
        self.path = path
        self.metadata = {}
        self.content = None
        self.page_count = 0

        # Validate file existence and type immediately
        self.validate_file()

    def validate_file(self) -> None:
        """
        Validates if the file exists, is a PDF, and is not corrupted.
        Raises exceptions if validation fails.
        """
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Error: The file '{self.path}' was not found.")

        if not self.path.lower().endswith('.pdf'):
            raise ValueError("Error: The selected file is not a valid PDF.")

        try:
            with fitz.open(self.path) as doc:
                self.page_count = len(doc)  # Check the number of pages
                if self.page_count == 0:
                    raise ValueError("Error: The PDF file is empty.")
        except Exception as e:
            raise ValueError(f"Error: The PDF file could not be read or is corrupted. Details: {e}")

    def load_file(self) -> None:
        """
        Loads the PDF content into memory.
        """
        try:
            with fitz.open(self.path) as doc:
                self.content = [page.get_text("text") for page in doc]  # Extracts text per page
        except Exception as e:
            raise Exception(f"Error while loading the PDF content: {e}")

    def get_metadata(self) -> dict:
        """
        Extracts and returns the metadata of the PDF file.
        :return: Dictionary containing metadata.
        """
        try:
            with fitz.open(self.path) as doc:
                meta = doc.metadata # Attribute that stocks metadatas
                self.metadata = {
                    "title": meta.get("title", "Unknown Title"),
                    "author": meta.get("author", "Unknown Author"),
                    "creation_date": meta.get("creationDate", "Unknown Date"),
                    "modification_date": meta.get("modDate", "Unknown Date"),
                    "page_count": self.page_count,
                }
                return self.metadata
        except Exception as e:
            raise Exception(f"Error extracting metadata: {e}")

    def is_encrypted(self) -> bool:
        """
        Checks if the PDF file is encrypted.
        :return: True if encrypted, False otherwise.
        """
        try:
            with fitz.open(self.path) as doc:
                return doc.is_encrypted
        except Exception as e:
            raise Exception(f"Error checking encryption: {e}")