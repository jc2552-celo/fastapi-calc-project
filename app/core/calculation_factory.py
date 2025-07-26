from abc import ABC, abstractmethod
from app.schemas.calculation import OperationType


class Operation(ABC):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    @abstractmethod
    def compute(self) -> float:
        pass


class Add(Operation):
    def compute(self) -> float:
        return self.a + self.b


class Sub(Operation):
    def compute(self) -> float:
        return self.a - self.b


class Mul(Operation):
    def compute(self) -> float:
        return self.a * self.b


class Div(Operation):
    def compute(self) -> float:
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b


class CalculationFactory:
    @staticmethod
    def get_operation(type_: OperationType, a: float, b: float) -> Operation:
        match type_:
            case OperationType.add:
                return Add(a, b)
            case OperationType.sub:
                return Sub(a, b)
            case OperationType.mul:
                return Mul(a, b)
            case OperationType.div:
                return Div(a, b)
            case _:
                raise ValueError(f"Unsupported operation type: {type_}")
