from pdf_parser.pdf_file import PDFFile
from pdf_parser.text_output import TextOutput
from pdf_parser.image_output import ImageOutput

class PDFParser:
    def __init__(self, pdf_file: PDFFile):
        """
        Initializes the PDFParser with a PDFFile instance.
        :param pdf_file: Instance of PDFFile to be parsed.
        """
        self.pdf_file = pdf_file
        self.text_output = None
        self.image_output = None

    def parse_text(self) -> TextOutput:
        """
        Parses the text content from the PDF file.
        :return: An instance of TextOutput containing the extracted text and page numbers.
        """
        # Example implementation using dummy data.
        # Replace this with an actual text extraction library like PyPDF2 or pdfminer.
        text_content = "Extracted text content from the PDF."
        page_numbers = [1, 2, 3]  # Example page numbers
        self.text_output = TextOutput(content=text_content, page_numbers=page_numbers)
        return self.text_output

    def parse_images(self) -> ImageOutput:
        """
        Parses the images from the PDF file.
        :return: An instance of ImageOutput containing the extracted images and page numbers.
        """
        # Example implementation using dummy data.
        # Replace this with an actual image extraction library like PyPDF2 or fitz (PyMuPDF).
        images = [b"image1_data", b"image2_data"]  # Example binary image data
        page_numbers = [1, 2]  # Example page numbers
        self.image_output = ImageOutput(images=images, page_numbers=page_numbers)
        return self.image_output

    def generate_outputs(self) -> None:
        """
        Generates both text and image outputs by parsing the PDF file.
        """
        self.parse_text()
        self.parse_images()
