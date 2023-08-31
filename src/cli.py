from typing import Union
from src.calculator import Calculator
from src.operations import Operations, Operator
from src.logger_mixin import LoggerMixin


class CLI(LoggerMixin):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()

    def start(self):
        self.logger.info("Starting calculator")
        while True:
            try:
                operator_str = self._get_operator()
                if self.check_quit(operator_str):
                    self.logger.info("Exiting calculator")
                    break
                operator = Operator(operator_str)
                self.logger.info("Operator chosen: ", operator=operator.value)

                first_number = self._get_prompt("Enter first number or q to quit: ")
                if self.check_quit(first_number):
                    self.logger.info("Exiting calculator")
                    break
                self.logger.info("First number entered: ", first_number=first_number)

                if operator in Operations.UNARY_OPERATORS:
                    second_number = None
                    result = self.calculator.execute(
                        operator,
                        first_number,
                    )
                else:
                    second_number = self._get_prompt("Enter second number or q to quit: ")
                    if self.check_quit(second_number):
                        self.logger.info("Exiting calculator")
                        break
                    self.logger.info("Second number entered: ", second_number=second_number)

                    result = self.calculator.execute(
                        operator,
                        first_number,
                        second_number
                    )

                formatted_result = self.format_result(
                    operator,
                    first_number,
                    second_number,
                    result
                )
                print(f"Result: {formatted_result}")

            except ZeroDivisionError as e:
                self.logger.error("Error encountered", error=str(e))
                print(f"Error: {str(e)}")
            except ValueError as e:
                self.logger.error("Error encountered", error=str(e))
                print(f"Error: {str(e)}")
            except Exception as e:
                self.logger.error("Error encountered", error=str(e))
                print(f"Error: {str(e)}")

    def format_result(
        self,
        operator: Operator,
        first_number: Union[float, str],
        second_number: Union[float, str, None],
        result: float
    ) -> str:
        if operator == Operator.FACTORIAL:
            return f"{first_number}! = {result}"
        elif operator == Operator.SQRT:
            return f"√{first_number} = {result}"
        else:
            return f"{first_number} {operator.value} {second_number} = {result}"
        
    def _get_prompt(
        self,
        prompt: str
    ) -> Union[float, str]:
        while True:
            value = input(prompt).strip()
            if self.check_quit(value):
                return 'q'
            try:
                return float(value)
            except ValueError:
                raise ValueError("Invalid number, try again")

    def _get_operator(self) -> Union[Operator, str]:
        while True:
            operator = input("Enter operator(+,-,*,**,/,sqrt,!,%,//): ").strip()
            if self.check_quit(operator):
                return 'q'
            try:
                return Operator(operator)
            except ValueError:
                raise ValueError("Invalid operator, try again")
            
    def check_quit(
        self,
        value: Union[float, str]
    ) -> bool:
        return value == 'q'
