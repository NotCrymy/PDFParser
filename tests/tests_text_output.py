import pytest
from pdf_parser.text_output import TextOutput

def test_text_output():
    """Test que l'objet TextOutput stocke bien le texte"""
    text = "This is a test text"
    text_output = TextOutput(text)

    assert text_output.content == text
