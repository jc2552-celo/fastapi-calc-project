# test_factory.py
from app.core.calculation_factory import CalculationFactory
from app.schemas.calculation import OperationType

calc = CalculationFactory.get_operation(OperationType.mul, 4, 5)
print(calc.compute())  # Should print 20
