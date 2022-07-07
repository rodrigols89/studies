from database import SessionLocal,engine
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud, models,schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/finance-data", response_model=list[schemas.FinanceData])
def read_financedata(
    skip: int=0,
    limit: int=1000,
    db: Session = Depends(get_db)
):
    finance_data = crud.get_financedata(db,skip=skip,limit=limit)
    return finance_data
