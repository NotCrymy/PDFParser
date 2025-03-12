import pytest
from pdf_parser.pdf_parser import PDFParser
from pdf_parser.pdf_file import PDFFile

@pytest.fixture
def mock_pdf():
    """Mock d'un objet PDFFile"""
    pdf = PDFFile("mock.pdf")
    pdf.content = b"Fake PDF content"
    return pdf

def test_parse_text(mock_pdf):
    """Test l'extraction de texte d'un PDF"""
    parser = PDFParser(mock_pdf)
    text_output = parser.parse_text()

    assert text_output is not None
    assert isinstance(text_output.content, str)

def test_parse_images(mock_pdf):
    """Test l'extraction des images d'un PDF"""
    parser = PDFParser(mock_pdf)
    image_output = parser.parse_images()

    assert image_output is not None
    assert isinstance(image_output.images, list)