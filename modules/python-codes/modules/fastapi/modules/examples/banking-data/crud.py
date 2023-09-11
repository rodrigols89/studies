from sqlalchemy.orm import Session
import models, schemas

def get_financedata(db: Session, skip: int=0,limit: int=1000):
 return db.query(models.FinanceData).offset(skip).limit(limit).all()
