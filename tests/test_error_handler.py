import pytest
from pdf_parser.error_handler import ErrorHandler

def test_log_error():
    """Test l'ajout d'une erreur dans le log"""
    error_handler = ErrorHandler()
    error_handler.log_error("Test error")

    errors = error_handler.get_errors()
    assert len(errors) == 1
    assert "Test error" in errors[0]
