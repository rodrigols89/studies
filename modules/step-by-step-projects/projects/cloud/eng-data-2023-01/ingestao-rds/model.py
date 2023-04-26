from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Coins(Base):
    __tablename__ = 'tb_coins'  # Se você usar instância "Base" é obrigatório.
    id = Column(Integer, primary_key=True)  # Obrigatório.
    name = Column(String)
    symbol = Column(String)
    data_added = Column(Text)
    last_updated = Column(Text)
    price = Column(Float)
    volume_24h = Column(Float)
    circulating_supply = Column(Float)
    total_supply = Column(Float)
    max_supply = Column(Float)
    volume_24h = Column(Float)
    percent_change_1h = Column(Float)
    percent_change_24h = Column(Float)
    percent_change_7d = Column(Float)


    def start():
        db_string = (
            'postgresql://postgres:7hRt5yU9pLm2@'
            'rds-server.c6qt8zkwdakp.us-east-1.rds.amazonaws.com/coins'
        )
        engine = create_engine(db_string)
        Session = sessionmaker(bind=engine)
        session = Session()
        Base.metadata.create_all(engine)
        print ('\nTable created on database')
        return session, engine
