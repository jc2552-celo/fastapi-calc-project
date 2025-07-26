from pydantic import BaseModel, Field, validator
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

    @validator("b")
    def no_division_by_zero(cls, value, values):
        if "type" in values and values["type"] == OperationType.div and value == 0:
            raise ValueError("Division by zero is not allowed.")
        return value


class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: OperationType
    result: Optional[float]

    class Config:
        orm_mode = True
