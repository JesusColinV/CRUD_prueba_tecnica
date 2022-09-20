from database.session import engine, SessionLocal
from database.base_class import Base


def create_database():
    return Base.metadata.create_all(bind=engine)

        
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()