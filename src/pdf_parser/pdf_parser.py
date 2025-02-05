import fitz
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
        Extracts text content from each page of the PDF.
        :return: An instance of TextOutput containing extracted text and page numbers.
        """
        extracted_text = []
        page_numbers = []

        try:
            with fitz.open(self.pdf_file.path) as doc:
                for page_num, page in enumerate(doc):
                    text = page.get_text("text")  # Extracts clean, formatted text
                    if text.strip():  # Avoid empty pages
                        extracted_text.append(f"Page {page_num + 1}:\n{text}\n")
                        page_numbers.append(page_num + 1)

            self.text_output = TextOutput(content="\n".join(extracted_text), page_numbers=page_numbers)
            return self.text_output

        except Exception as e:
            raise Exception(f"Error while extracting text: {e}")

    def parse_images(self) -> ImageOutput:
        """
        Extracts images from the PDF pages.
        :return: An instance of ImageOutput containing extracted images and page numbers.
        """
        extracted_images = []
        page_numbers = []

        try:
            with fitz.open(self.pdf_file.path) as doc:
                for page_num, page in enumerate(doc):
                    images = page.get_images(full=True)  # Get all images
                    for img_index, img in enumerate(images):
                        xref = img[0]  # Image reference ID
                        base_image = doc.extract_image(xref)  # Extract raw image
                        image_bytes = base_image["image"]  # Get image bytes
                        extracted_images.append(image_bytes)
                        page_numbers.append(page_num + 1)

            self.image_output = ImageOutput(images=extracted_images, page_numbers=page_numbers)
            return self.image_output

        except Exception as e:
            raise Exception(f"Error while extracting images: {e}")

    def generate_outputs(self) -> None:
        """
        Parses both text and images from the PDF and stores them in respective output objects.
        """
        self.parse_text()
        self.parse_images()