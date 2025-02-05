class TextOutput:
    def __init__(self, content: str, page_numbers: list[int]):
        """
        Initializes a TextOutput instance with extracted text and associated page numbers.
        :param content: Extracted text content.
        :param page_numbers: List of page numbers where the text was extracted.
        """
        self.content = content

    def get_content(self) -> str:
        """
        Returns the full extracted text from the PDF.
        :return: A string containing the entire extracted text.
        """
        return self.content