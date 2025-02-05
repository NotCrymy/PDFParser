import os
import csv
from pdf_parser.text_output import TextOutput
from pdf_parser.image_output import ImageOutput

class ExportManager:
    def __init__(self):
        """
        Initializes the ExportManager with no outputs initially.
        """
        self.text_outputs = []
        self.image_outputs = []

    def _ensure_output_directory(self, file_path: str) -> None:
        """
        Ensures that the output directory exists before writing files.
        :param file_path: Path where the file will be saved.
        """
        output_dir = os.path.dirname(file_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)  # Automatically create output/ directory

    def export_to_txt(self, output_path: str) -> None:
        """
        Exports the text outputs to a TXT file.
        :param output_path: Path to save the exported TXT file.
        """
        try:
            self._ensure_output_directory(output_path)
            with open(output_path, 'w', encoding='utf-8') as file:
                for text_output in self.text_outputs:
                    file.write(text_output.content + "\n\n")
            print(f"Text successfully exported to {output_path}")
        except Exception as e:
            raise Exception(f"Error exporting to TXT: {e}")

    def export_to_csv(self, output_path: str) -> None:
        """
        Exports the text outputs to a CSV file.
        :param output_path: Path to save the exported CSV file.
        """
        try:
            self._ensure_output_directory(output_path)
            with open(output_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Page", "Text Content"])
                for text_output in self.text_outputs:
                    writer.writerow(["N/A", text_output.content])  # No pagination
            print(f"Text successfully exported to {output_path}")
        except Exception as e:
            raise Exception(f"Error exporting to CSV: {e}")

    def export_images(self, output_dir: str) -> None:
        """
        Exports the extracted images to the specified directory.
        :param output_dir: Directory to save the exported images.
        """
        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)  # Automatically create output/images/ directory

            for i, image_output in enumerate(self.image_outputs):
                for j, image in enumerate(image_output.images):
                    image_path = os.path.join(output_dir, f"image_{i+1}_{j+1}.png")
                    with open(image_path, 'wb') as file:
                        file.write(image)
            print(f"Images successfully exported to {output_dir}")

        except Exception as e:
            raise Exception(f"Error exporting images: {e}")