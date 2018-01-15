from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Float
from sqlalchemy import ForeignKey

from MinProd import app
# from MinProd.server.models.base import Base


Base = declarative_base()

# https://www.bankrate.com/calculators/mortgages/loan-calculator.aspx
class Loan(Base):
    __tablename__   = 'Loan'
    id              = Column(Integer, primary_key=True)
    apr             = Column(Float)
    years           = Column(Float)
    amount          = Column(Float)
    date_created    = Column(DateTime, nullable=False)
    date_modified   = Column(DateTime, nullable=False)
    created_by  = Column(Integer, ForeignKey('User.id'), nullable=False)
    modified_by = Column(Integer, ForeignKey('User.id'), nullable=False)


    # Payments --------------------------------------------------------
    @staticmethod
    def calc_monthly_payment(apr, years, amount):
        # pmt = (r * PV) / (1 - (1 + r)^-n)
        payment = (apr/12)*amount / (1 - (1 + apr/12)**-(years*12))
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
    def calc_total_interest(apr, years, amount):
        total_interest = Loan.calc_total_cost(apr, years, amount)
        total_interest = total_interest - amount
        return round(total_interest, 2)


    @staticmethod
    def calc_interest_paid():
        return None


    @staticmethod
    def calc_interest_remaining():
        return None


    # Totals --------------------------------------------------------
    @staticmethod
    def calc_total_cost(apr, years, amount):
        total_cost = Loan.calc_monthly_payment(apr, years, amount) 
        total_cost = total_cost * 12 * years
        return round(total_cost, 2)


    @staticmethod
    def calc_total_remaining(apr, years, amount, current_period):
        # http://financeformulas.net/Remaining_Balance_Formula.html
        t = current_period

        total_payments = Loan.calc_monthly_payment(apr, years, amount)
        total_payments = total_payments * ( ((1 + apr)**t - 1) / apr )

        total_remaining = Loan.calc_total_cost(apr, years, amount)
        total_remaining = total_remaining - total_payments

        return round(total_remaining, 2)


    # Charting --------------------------------------------------------
    @staticmethod
    def calc_amortization_schedule():
        return None
