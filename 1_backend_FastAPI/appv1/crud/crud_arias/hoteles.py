from sqlalchemy.orm import Session
from models import Hotel

def get_hoteles(db: Session):
    return db.query(Hotel).all()
