import pytest
from app.core.calculation_factory import CalculationFactory
from app.schemas.calculation import CalculationCreate, OperationType


# -------------------------------
# Factory Tests
# -------------------------------

def test_add_operation():
    calc = CalculationFactory.get_operation(OperationType.add, 10, 5)
    assert calc.compute() == 15


def test_subtract_operation():
    calc = CalculationFactory.get_operation(OperationType.sub, 10, 5)
    assert calc.compute() == 5


def test_multiply_operation():
    calc = CalculationFactory.get_operation(OperationType.mul, 10, 5)
    assert calc.compute() == 50


def test_divide_operation():
    calc = CalculationFactory.get_operation(OperationType.div, 10, 2)
    assert calc.compute() == 5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        CalculationFactory.get_operation(OperationType.div, 10, 0).compute()


# -------------------------------
# Pydantic Schema Validation Tests
# -------------------------------

def test_valid_calculation_create():
    schema = CalculationCreate(a=10, b=2, type=OperationType.div)
    assert schema.a == 10
    assert schema.b == 2
    assert schema.type == OperationType.div


def test_invalid_division_by_zero_schema():
    with pytest.raises(ValueError) as exc:
        CalculationCreate(a=10, b=0, type=OperationType.div)
    assert "Division by zero is not allowed." in str(exc.value)


def test_invalid_type_enum():
    with pytest.raises(ValueError):
        CalculationCreate(a=10, b=5, type="Exponent")  # Not a valid OperationType
