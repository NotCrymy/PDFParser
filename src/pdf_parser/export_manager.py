from pdf_parser.text_output import TextOutput
from pdf_parser.image_output import ImageOutput

class ExportManager:
    def __init__(self):
        """
        Initializes the ExportManager with no outputs initially.
        """
        self.text_outputs = []
        self.image_outputs = []

    def export_to_csv(self, output_path: str) -> None:
        """
        Exports the text outputs to a CSV file.
        :param output_path: Path to save the exported CSV file.
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                for text_output in self.text_outputs:
                    for page_number in text_output.page_numbers:
                        file.write(f"Page {page_number}: {text_output.content}\n")
        except Exception as e:
            raise Exception(f"Error exporting to CSV: {e}")

    def export_to_txt(self, output_path: str) -> None:
        """
        Exports the text outputs to a TXT file.
        :param output_path: Path to save the exported TXT file.
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                for text_output in self.text_outputs:
                    file.write(text_output.content + "\n")
        except Exception as e:
            raise Exception(f"Error exporting to TXT: {e}")

    def export_images(self, output_path: str) -> None:
        """
        Exports the image outputs to the specified directory.
        :param output_path: Directory to save the exported images.
        """
        import os
        try:
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            for i, image_output in enumerate(self.image_outputs):
                for j, image in enumerate(image_output.images):
                    image_path = os.path.join(output_path, f"image_{i+1}_{j+1}.png")
                    with open(image_path, 'wb') as file:
                        file.write(image)
        except Exception as e:
            raise Exception(f"Error exporting images: {e}")
