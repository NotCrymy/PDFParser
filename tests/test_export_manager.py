import pytest
import os
from pdf_parser.export_manager import ExportManager
from pdf_parser.text_output import TextOutput

@pytest.fixture
def sample_text_output():
    """Crée une sortie texte fictive pour le test"""
    return TextOutput("Sample text content")

def test_export_to_txt(tmp_path, sample_text_output):
    """Test l'exportation d'un fichier texte"""
    export_manager = ExportManager()
    output_path = tmp_path / "output.txt"

    export_manager.text_outputs.append(sample_text_output)
    export_manager.export_to_txt(str(output_path))

    assert os.path.exists(output_path)
    with open(output_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Sample text content" in content
