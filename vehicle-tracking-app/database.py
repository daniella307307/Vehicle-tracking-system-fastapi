from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,registry


DATABASE_URL = "mysql+pymysql://root:@localhost:3306/vehicle_tracking"
mapper_registry= registry()
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
mapper_registry.configure()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



Base = mapper_registry.generate_base()
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
