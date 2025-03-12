import pytest
import os
from pdf_parser.import_manager import ImportManager
from pdf_parser.pdf_file import PDFFile

@pytest.fixture
def sample_pdf(tmp_path):
    """Crée un fichier PDF temporaire pour les tests"""
    pdf_path = tmp_path / "test.pdf"
    with open(pdf_path, "wb") as f:
        f.write(b"%PDF-1.4")
    return str(pdf_path)

def test_import_valid_pdf(sample_pdf):
    """Test l'importation d'un fichier PDF valide"""
    import_manager = ImportManager()
    pdf_file = import_manager.import_file(sample_pdf)

    assert isinstance(pdf_file, PDFFile)
    assert pdf_file.path == sample_pdf

def test_import_nonexistent_pdf():
    """Test l'importation d'un fichier qui n'existe pas"""
    import_manager = ImportManager()
    with pytest.raises(FileNotFoundError):
        import_manager.import_file("fake.pdf")
