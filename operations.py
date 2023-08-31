import math
from enum import Enum
from typing import Callable
from logger_mixin import LoggerMixin

class Operator(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    POWER = "**"
    SQRT = "sqrt"
    FACTORIAL = "!"
    MODULUS = "%"
    INT_DIVIDE = "//"


class Operations(LoggerMixin):
    UNARY_OPERATORS = {
        Operator.SQRT,
        Operator.FACTORIAL
    }

    @staticmethod
    def binary_operation(
        fn: Callable
    ) -> Callable:
        return fn

    @staticmethod
    def unary_operation(
        fn: Callable
    ) -> Callable:
        return fn

    @staticmethod
    def add(
        first: float,
        second: float
    ) -> float:
        return first + second

    @staticmethod
    def subtract(
        first: float,
        second: float
    ) -> float:
        return first - second

    @staticmethod
    def multiply(
        first: float,
        second: float
    ) -> float:
        return first * second

    @staticmethod
    def divide(
        first: float,
        second: float
    ) -> float:
        if second == 0:
            raise ZeroDivisionError("You can't divide by zero")
        return first / second

    @staticmethod
    def int_divide(
        first: float,
        second: float
    ) -> float:
        if second == 0:
            raise ZeroDivisionError("You can't divide by zero")
        return first // second

    @staticmethod
    def power(
        first: float,
        second: float
    ) -> float:
        return first ** second

    @staticmethod
    def modulus(
        first: float,
        second: float
    ) -> float:
        return first % second

    @staticmethod
    def sqrt(number: float) -> float:
        if number < 0:
            raise ValueError(
                "You can't take the square root of a negative number"
            )
        return math.sqrt(number)

    @staticmethod
    def factorial(number: float) -> int:
        if number < 0:
            raise ValueError(
                "You can't take the factorial of a negative number"
            )
        if number == int(number):
            return math.factorial(int(number))
        else:
            return math.gamma(number + 1)
