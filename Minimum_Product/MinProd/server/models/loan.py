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
    created_by = Column(Integer, ForeignKey('User.id'), nullable=False)
    modified_by = Column(Integer, ForeignKey('User.id'), nullable=False)


    # Payments --------------------------------------------------------
    @staticmethod
    def calc_monthly_payment(yearly_rate, length_years, loan_amount):
        # pmt = (r * PV) / (1 - (1 + r)^-n)
        period_rate = float(yearly_rate) / 12
        periods = int(length_years) * 12
        pv = float(loan_amount)

        payment = period_rate * pv / (1 - (1 + period_rate) ** -periods)
        return round(payment, 2)


    @staticmethod
    def calc_payment_ppart():
        return None


    @staticmethod
    def calc_payment_ipart():
        return None


    # Principle -------------------------------------------------------
    @staticmethod
    def calc_principle_paid():
        return None


    @staticmethod
    def calc_principle_remaining():
        return None


    # Interest --------------------------------------------------------
    @staticmethod
    def calc_total_interest():
        return None


    @staticmethod
    def calc_interest_paid():
        return None


    @staticmethod
    def calc_interest_remaining():
        return None


    @staticmethod
    def calc_total_cost():
        total_cost = principle + calc_total_interest()
        return LoanView.display_total_cost(total_cost)


    # Charting --------------------------------------------------------
    @staticmethod
    def calc_amortization_schedule():
        return None
