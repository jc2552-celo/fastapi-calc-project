from pydantic import BaseModel, model_validator
from enum import Enum
from typing import Optional


class OperationType(str, Enum):
    add = "Add"
    sub = "Sub"
    mul = "Multiply"
    div = "Divide"


class CalculationCreate(BaseModel):
    a: float
    b: float
    type: OperationType

    @model_validator(mode="after")
    def validate_division(self) -> 'CalculationCreate':
        if self.type == OperationType.div and self.b == 0:
            raise ValueError("Division by zero is not allowed.")
        return self


class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: OperationType
    result: Optional[float]

    model_config = {
        "from_attributes": True
    }

