import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.schemas.calculation import CalculationCreate, OperationType
from app.crud.calculation import create_calculation, get_calculation


# Use the same DB your Docker container runs (clean or throwaway data is fine for now)
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.rollback()
    db.close()


def test_create_and_get_calculation(db):
    data = CalculationCreate(a=10, b=5, type=OperationType.add)
    new_calc = create_calculation(db, data)
    fetched = get_calculation(db, new_calc.id)

    assert fetched is not None
    assert fetched.id == new_calc.id
    assert fetched.result == 15
    assert fetched.type == OperationType.add
