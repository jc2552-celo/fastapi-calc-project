from sqlalchemy.orm import Session
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate
from app.core.calculation_factory import CalculationFactory


def create_calculation(db: Session, data: CalculationCreate) -> Calculation:
    operation = CalculationFactory.get_operation(data.type, data.a, data.b)
    result = operation.compute()

    calc = Calculation(a=data.a, b=data.b, type=data.type, result=result)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    return calc


def get_calculation(db: Session, calc_id: int) -> Calculation | None:
    return db.query(Calculation).filter(Calculation.id == calc_id).first()
