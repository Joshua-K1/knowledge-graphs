from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
import json

# declare the base class
Base = declarative_base()

# project model
class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String, nullable=False)
    
    # Relationship to Application (one project can have many applications)
    applications = relationship("Application", back_populates="project")


# database dependencies
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

