import os
import csv
import shutil
from pdf_parser.text_output import TextOutput
from pdf_parser.image_output import ImageOutput

class ExportManager:
    def __init__(self):
        """
        Initializes the ExportManager with no outputs initially and ensures output directory is clean.
        """
        self.text_outputs = []
        self.image_outputs = []
        self.output_dir = "output/"  # Central output directory
        self._purge_output_directory()  # Ensure the directory is empty at initialization

    def _purge_output_directory(self) -> None:
        """
        Deletes all existing files and directories inside the output folder.
        This only runs ONCE when ExportManager is instantiated.
        """
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)  # Delete entire output folder
        os.makedirs(self.output_dir)  # Recreate it empty

    def export_to_txt(self, output_path: str) -> None:
        """
        Exports the text outputs to a TXT file.
        :param output_path: Path to save the exported TXT file.
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                for text_output in self.text_outputs:
                    file.write(text_output.content + "\n\n")
            print(f"Text successfully exported to {output_path}")
        except Exception as e:
            raise Exception(f"Error exporting to TXT: {e}")

    def export_images(self, output_dir: str) -> None:
        """
        Exports the extracted images to the specified directory.
        :param output_dir: Directory to save the exported images.
        """
        try:
            os.makedirs(output_dir, exist_ok=True)  # Ensure the images directory exists

            for i, image_output in enumerate(self.image_outputs):
                for j, image in enumerate(image_output.images):
                    image_path = os.path.join(output_dir, f"image_{i+1}_{j+1}.png")
                    with open(image_path, 'wb') as file:
                        file.write(image)
            print(f"Images successfully exported to {output_dir}")

        except Exception as e:
            raise Exception(f"Error exporting images: {e}")