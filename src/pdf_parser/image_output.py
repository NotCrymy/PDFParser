class ImageOutput:
    def __init__(self, images: list[bytes], page_numbers: list[int]):
        """
        Initializes an ImageOutput instance with extracted images and associated page numbers.
        :param images: List of binary image data.
        :param page_numbers: List of page numbers where the images were extracted.
        """
        self.images = images
        self.page_numbers = page_numbers

    def get_image_count(self) -> int:
        """
        Returns the number of images extracted.
        :return: The count of images.
        """
        return len(self.images)

    def save_images(self, output_path: str) -> None:
        """
        Saves all images to the specified directory.
        :param output_path: Path to the directory where the images will be saved.
        """
        import os
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        for i, image in enumerate(self.images):
            image_path = os.path.join(output_path, f"image_{i+1}.png")
            with open(image_path, 'wb') as file:
                file.write(image)
