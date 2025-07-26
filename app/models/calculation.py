from sqlalchemy import Column, Integer, Float, Enum
from app.database import Base
from app.schemas.calculation import OperationType


class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    type = Column(Enum(OperationType), nullable=False)
    result = Column(Float, nullable=True)
