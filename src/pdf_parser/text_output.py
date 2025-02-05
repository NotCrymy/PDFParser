class TextOutput:
    def __init__(self, content: str, page_numbers: list[int]):
        """
        Initializes a TextOutput instance with extracted text and associated page numbers.
        :param content: The extracted text content.
        :param page_numbers: List of page numbers where the text was extracted.
        """
        self.content = content
        self.page_numbers = page_numbers

    def get_summary(self) -> str:
        """
        Returns a summary of the text content (first 100 characters).
        :return: A string containing the summary.
        """
        return self.content[:100] + ("..." if len(self.content) > 100 else "")

    def search_keyword(self, keyword: str) -> list[int]:
        """
        Searches for a keyword in the text content and returns the page numbers where it's found.
        :param keyword: The keyword to search for.
        :return: List of page numbers containing the keyword.
        """
        if keyword.lower() in self.content.lower():
            return self.page_numbers
        return []
