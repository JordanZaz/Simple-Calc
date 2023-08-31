from logger_mixin import LoggerMixin
from typing import Optional
from operations import Operations, Operator


class Calculator(LoggerMixin):
    def __init__(self):
        super().__init__()
        self.operations_util = Operations()

    def execute(
        self,
        operator: Operator,
        first_number: float,
        second_number: Optional[float] = None
    ) -> float:
        self.bind_logger(
            operator=operator.value,
            first_number=first_number,
            second_number=second_number
        )

        if operator in Operations.UNARY_OPERATORS:
            op_func = self.operations_util.unary_operation(
                getattr(self.operations_util, operator.name.lower()))
            
            result = op_func(first_number)
        else:
            op_func = self.operations_util.binary_operation(
                getattr(self.operations_util, operator.name.lower()))
            
            result = op_func(first_number, second_number)

        self.logger.info(
            "Operation executed",
            result=result
        )

        return result
