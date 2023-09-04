import pytest
from unittest.mock import patch, Mock
from calculator.src.cli import CLI

def test_valid_followed_by_invalid_input() -> None:
    mock_logger = Mock()
    
    with patch('structlog.get_logger', return_value=mock_logger):
        with patch('builtins.input', side_effect=['+', 'a', 'q']):
            cli = CLI()
            cli.start()

    mock_logger.error.assert_called_with(
        "Error encountered", error="Invalid number, try again")
    
def test_repeated_invalid_inputs() -> None:
    mock_logger = Mock()

    with patch ('structlog.get_logger', return_value=mock_logger):
        with patch('builtins.input', side_effect=['a', 'a', 'a', 'q']):
            cli = CLI()
            cli.start()

    mock_logger.error.call_count == 3
