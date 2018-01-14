from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Float
from sqlalchemy import ForeignKey

from MinProd import app
# from MinProd.server.models.base import Base


Base = declarative_base()

class Loan(Base):
    __tablename__   = 'Loan'
    id              = Column(Integer, primary_key=True)
    yearly_rate     = Column(Float)
    length_years    = Column(Integer)
    loan_amount     = Column(Float)
    date_created    = Column(DateTime, nullable=False)
    date_modified   = Column(DateTime, nullable=False)
    created_by = Column(Integer, ForeignKey("User.id"), nullable=False)
    modified_by = Column(Integer, ForeignKey("User.id"), nullable=False)
