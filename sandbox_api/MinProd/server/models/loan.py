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
    def calc_payment(apr, years, amount, yearly_compounds):
        # Formula is: pmt = (r * PV) / (1 - (1 + r)^-n)

        # calc initial vars
        period_rate = apr / yearly_compounds
        count_periods = years * yearly_compounds

        # calc payment
        payment = period_rate * amount / \
            (1 - (1 + period_rate) ** -count_periods)

        return round(payment, 2)


    @staticmethod
    def calc_payment_ppart(
        apr, years, amount, yearly_compounds, current_period):

        amort_sched = Loan.amortize_loan(
            apr, years, amount, yearly_compounds)

        return amort_sched[current_period][2]


    @staticmethod
    def calc_payment_ipart(
        apr, years, amount, yearly_compounds, current_period):
        
        amort_sched = Loan.amortize_loan(
            apr, years, amount, yearly_compounds)

        return amort_sched[current_period][1]


    # Principle -------------------------------------------------------
    @staticmethod
    def calc_principle_paid(
        apr, years, amount, yearly_compounds, current_period):

        amort_sched = Loan.amortize_loan(
            apr, years, amount, yearly_compounds)

        period = 1
        principle_paid = 0

        while (period <= current_period):
            principle_paid = principle_paid + amort_sched[period][2]
            period = period + 1

        return principle_paid


    @staticmethod
    def calc_principle_remaining(
        apr, years, amount, yearly_compounds, current_period):

        amort_sched = Loan.amortize_loan(
            apr, years, amount, yearly_compounds)

        period = current_period + 1
        prin_remain = 0

        while (period <= years * yearly_compounds):
            prin_remain = prin_remain + amort_sched[period][2]
            period = period + 1

        return prin_remain


    # Interest --------------------------------------------------------
    @staticmethod
    def calc_total_interest(apr, years, amount, yearly_compounds):
        total_interest = Loan.calc_total_cost(
            apr, years, amount, yearly_compounds)

        return round(total_interest - amount, 2)


    @staticmethod
    def calc_interest_paid(
        apr, years, amount, yearly_compounds, current_period):

        amort_sched = Loan.amortize_loan(
            apr, years, amount, yearly_compounds)

        period = 1
        interest_paid = 0

        while (period <= current_period):
            interest_paid = interest_paid + amort_sched[period][1]
            period = period + 1

        return interest_paid

    @staticmethod
    def calc_interest_remaining(
        apr, years, amount, yearly_compounds, current_period):

        amort_sched = Loan.amortize_loan(
            apr, years, amount, yearly_compounds)

        period = current_period + 1
        interest_remain = 0

        while (period <= years * yearly_compounds):
            interest_remain = interest_remain + amort_sched[period][1]
            period = period + 1

        return round(interest_remain,2)


    # Totals ----------------------------------------------------------
    @staticmethod
    def calc_total_cost(apr, years, amount, yearly_compounds):
        total_cost = Loan.calc_payment(
            apr, years, amount, yearly_compounds) 

        total_cost = total_cost * yearly_compounds * years
        return round(total_cost, 2)


    @staticmethod
    def calc_total_remaining(
        apr, years, amount, yearly_compounds, current_period):
        # http://financeformulas.net/Remaining_Balance_Formula.html
        t = current_period

        total_payments = Loan.calc_payment(
            apr, years, amount, yearly_compounds)

        total_payments = total_payments * ( ((1 + apr)**t - 1) / apr )

        total_remaining = Loan.calc_total_cost(
            apr, years, amount, yearly_compounds)

        total_remaining = total_remaining - total_payments

        return round(total_remaining, 2)


    # Dates ----------------------------------------------------------
    @staticmethod
    def estimate_payoff_date():
        return 0


    # Charting --------------------------------------------------------
    @staticmethod
    def amortize_loan(apr, years, amount, yearly_compounds):
        # TODO: Replace with pandas
        
        # calc initial vars
        pmt = Loan.calc_payment(apr, years, amount, yearly_compounds)
        period_rate = apr / yearly_compounds
        count_periods = years * yearly_compounds

        # dict is the follow: {period, [pmt, ipmt, ppmt, balance]}
        amort_sched = {}
        amort_sched[0] = [0, 0, 0, amount]

        period = 1
        while (period <= count_periods):
            # get period payment parts and balance
            ipmt = round(amort_sched[period-1][3] * period_rate, 2)
            ppmt = round(pmt - ipmt, 2)
            balance = round(amort_sched[period-1][3] - ppmt, 2)

            # save and move to next period
            amort_sched[period] = [pmt, ipmt, ppmt, balance]
            period = period + 1

        return amort_sched
