from sqlalchemy import Column, Float, Integer, VARCHAR
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class HeroModel(Base):
    __tablename__ = "hero"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    npc_name = Column(VARCHAR(50), nullable=False)
    primary_attr = Column(VARCHAR(50), nullable=False)
    attack_type = Column(VARCHAR(50), nullable=False)
    img = Column(VARCHAR(100), nullable=False)
    icon = Column(VARCHAR(100), nullable=False)
    base_health = Column(Float, nullable=False)
    base_health_regen = Column(Float, nullable=False)
    base_mana = Column(Float, nullable=False)
    base_mana_regen = Column(Float, nullable=False)
    base_armor = Column(Float, nullable=False)
    base_attack_min = Column(Float, nullable=False)
    base_attack_max = Column(Float, nullable=False)
    base_str = Column(Float, nullable=False)
    base_agi = Column(Float, nullable=False)
    base_int = Column(Float, nullable=False)
    str_gain = Column(Float, nullable=False)
    agi_gain = Column(Float, nullable=False)
    int_gain = Column(Float, nullable=False)
    attack_range = Column(Float, nullable=False)
    projectile_speed = Column(Float, nullable=False)
    move_speed = Column(Float, nullable=False)
    legs = Column(Integer, nullable=False)


class StudentModel(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    lastname = Column(VARCHAR(50), nullable=False)


if __name__ == "__main__":
    
    # Database settings
    username = "root"
    password = "toor"
    database = "mysql-db"
    host="localhost"
    port="3310"

    # Make an Engine.    
    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}",
        echo=True,
    )

    Base.metadata.create_all(engine)
