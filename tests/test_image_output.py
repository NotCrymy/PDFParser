import pytest
from pdf_parser.image_output import ImageOutput

def test_image_output():
    """Test que l'objet ImageOutput stocke bien les images"""
    images = [b"image1_data", b"image2_data"]
    image_output = ImageOutput(images)

    assert len(image_output.images) == 2
    assert image_output.images[0] == b"image1_data"
