import pytest
from unittest.mock import patch, Mock, call
from calculator.src.cli import CLI

def test_cli_logger_called_correctly() -> None:
    mock_logger = Mock()
    with patch('structlog.get_logger', return_value=mock_logger):
        with patch('builtins.input', side_effect=['+', '2', '2', 'q']):
            cli = CLI()
            cli.start()
    mock_logger.info.assert_has_calls([
        call("Starting calculator"),
        call("Operator chosen: ", operator='+'),
        call("First number entered: ", first_number=2.0),
        call("Second number entered: ", second_number=2.0),
        call("Exiting calculator"),
    ])
