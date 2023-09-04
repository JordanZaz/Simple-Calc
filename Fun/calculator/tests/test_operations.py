import pytest
from unittest.mock import patch, Mock
from calculator.src.operations import Operator
from calculator.src.cli import CLI
from calculator.src.calculator import Calculator

def test_add() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.ADD,
        first_number=2,
        second_number=2
    )
    assert result == 4.0

def test_add_false_values() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.ADD,
        first_number=2,
        second_number=2
    )
    false_values = [1, 2, 3, 5, 6, -1, -2]
    for value in false_values:
        assert result != value

def test_wrong_number_input() -> None:
    mock_logger = Mock()
    
    with patch('structlog.get_logger', return_value=mock_logger):
        with patch('builtins.input', side_effect=['+', 'a', 'q']):
            cli = CLI()
            cli.start()

    mock_logger.error.assert_called_with(
        "Error encountered", error="Invalid number, try again")

def test_wrong_operator_input() -> None:
    mock_logger = Mock()
    
    with patch('structlog.get_logger', return_value=mock_logger):
        with patch('builtins.input', side_effect=['a', '2', '2', 'q']):
            cli = CLI()
            cli.start()

    mock_logger.error.assert_called_with(
        "Error encountered", error="Invalid operator, try again")

def test_subtract() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.SUBTRACT,
        first_number=2,
        second_number=2
    )
    assert result == 0

def test_subtract_false_values() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.SUBTRACT,
        first_number=2,
        second_number=2
    )
    false_values = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
    for value in false_values:
        assert result != value

def test_multiply() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.MULTIPLY,
        first_number=2,
        second_number=3
    )
    assert result == 6

def test_multiply_false_values() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.MULTIPLY,
        first_number=2,
        second_number=3
    )
    false_values = [1, 2, 3, 4, 5, 7, 8, -1, -2]
    for value in false_values:
        assert result != value

def test_divide() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.DIVIDE,
        first_number=6,
        second_number=2
    )
    assert result == 3

def test_divide_false_values() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.DIVIDE,
        first_number=6,
        second_number=2
    )
    false_values = [1, 2, 4, 5, 6]
    for value in false_values:
        assert result != value

def test_divide_by_zero() -> None:
    mock_logger = Mock()
    
    with patch('structlog.get_logger', return_value=mock_logger):
        with patch('builtins.input', side_effect=['/', '2', '0', 'q']):
            cli = CLI()
            cli.start()

    mock_logger.error.assert_called_with(
        "Error encountered", error="You can't divide by zero")

def test_int_divide() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.INT_DIVIDE,
        first_number=7,
        second_number=2
    )
    assert result == 3

def test_int_divide_false_values() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.INT_DIVIDE,
        first_number=7,
        second_number=2
    )
    false_values = [1, 2, 4, 5, 6, 7]
    for value in false_values:
        assert result != value

def test_int_divide_by_zero() -> None:
    mock_logger = Mock()
    
    with patch('structlog.get_logger', return_value=mock_logger):
        with patch('builtins.input', side_effect=['//', '2', '0', 'q']):
            cli = CLI()
            cli.start()

    mock_logger.error.assert_called_with(
        "Error encountered", error="You can't divide by zero")

def test_power() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.POWER,
        first_number=2,
        second_number=3
    )
    assert result == 8

def test_power_false_values() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.POWER,
        first_number=2,
        second_number=3
    )
    false_values = [1, 2, 3, 4, 5, 7, 9, 10, -1, -2]
    for value in false_values:
        assert result != value

def test_power_of_zero() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.POWER,
        first_number=2,
        second_number=0
    )
    assert result == 1

def test_zero_power_n() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.POWER,
        first_number=0,
        second_number=2
    )
    assert result == 0

def test_modulus() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.MODULUS,
        first_number=7,
        second_number=2
    )
    assert result == 1

def test_modulus_false_values() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.MODULUS,
        first_number=7,
        second_number=2
    )
    false_values = [0, 2, 3, 4, 5, 6, 7]
    for value in false_values:
        assert result != value

def test_sqrt() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.SQRT,
        first_number=4
    )
    assert result == 2

def test_sqrt_negative_value() -> None:
    mock_logger = Mock()
    
    with patch('structlog.get_logger', return_value=mock_logger):
        with patch('builtins.input', side_effect=['sqrt', '-4', 'q']):
            cli = CLI()
            cli.start()

    mock_logger.error.assert_called_with(
        "Error encountered", error="You can't take the square root of a negative number")

def test_factorial() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.FACTORIAL,
        first_number=4
    )
    assert result == 24

def test_factorial_negative_value() -> None:
    mock_logger = Mock()
    
    with patch('structlog.get_logger', return_value=mock_logger):
        with patch('builtins.input', side_effect=['!', '-4', 'q']):
            cli = CLI()
            cli.start()

    mock_logger.error.assert_called_with(
        "Error encountered", error="You can't take the factorial of a negative number")
    
def test_factorial_decimal_value() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.FACTORIAL,
        first_number=3.5
    )
    assert result == 11.631728396567452

def test_large_numbers() -> None:
    calculator = Calculator()
    result = calculator.execute(
        operator=Operator.ADD,
        first_number=1e300,
        second_number=1e300
    )
    assert result == 2e300
