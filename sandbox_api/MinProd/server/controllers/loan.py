from MinProd import app
from MinProd.server.models.loan import Loan
from MinProd.server.views.loan import LoanView


class LoanController():
    # Payments --------------------------------------------------------
    @staticmethod
    def get_payment(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        yearly_compounds = loan_terms['yearly_compounds']

        return LoanView.display_basic('Payment', 
            Loan.calc_payment(rate, years, amount, yearly_compounds))


    @staticmethod
    def get_payment_ppart(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        yearly_compounds = loan_terms['yearly_compounds']
        current_period = loan_terms['current_period']

        return LoanView.display_basic('Principle Part', 
            Loan.calc_payment_ppart(
                rate, years, amount, yearly_compounds, current_period))


    @staticmethod
    def get_payment_ipart(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        yearly_compounds = loan_terms['yearly_compounds']
        current_period = loan_terms['current_period']

        return LoanView.display_basic('Interest Part',
            Loan.calc_payment_ipart(
                rate, years, amount, yearly_compounds, current_period))


    # Principle -------------------------------------------------------
    @staticmethod
    def get_principle_paid(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        yearly_compounds = loan_terms['yearly_compounds']
        current_period = loan_terms['current_period']

        return LoanView.display_basic('Principle Paid',
            Loan.calc_principle_paid(
                rate, years, amount, yearly_compounds, current_period))


    @staticmethod
    def get_principle_remaining(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        yearly_compounds = loan_terms['yearly_compounds']
        current_period = loan_terms['current_period']

        return LoanView.display_basic('Principle Remaining',
            Loan.calc_principle_remaining(
                rate, years, amount, yearly_compounds, current_period))


    # Interest --------------------------------------------------------
    @staticmethod
    def get_total_interest(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        yearly_compounds = loan_terms['yearly_compounds']

        return LoanView.display_basic('Total Interest',
            Loan.calc_total_interest(
                rate, years, amount, yearly_compounds))


    @staticmethod
    def get_interest_paid(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        yearly_compounds = loan_terms['yearly_compounds']
        current_period = loan_terms['current_period']

        return LoanView.display_basic('Interest Paid',
            Loan.calc_interest_paid(
                rate, years, amount, yearly_compounds, current_period))


    @staticmethod
    def get_interest_remaining(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        yearly_compounds = loan_terms['yearly_compounds']
        current_period = loan_terms['current_period']

        return LoanView.display_basic('Interest Remaining',
            Loan.calc_interest_remaining(
                rate, years, amount, yearly_compounds, current_period))


    # Totals --------------------------------------------------------
    @staticmethod
    def get_total_cost(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        yearly_compounds = loan_terms['yearly_compounds']

        return LoanView.display_basic('Total Cost',
            Loan.calc_total_cost(
                rate, years, amount, yearly_compounds))


    @staticmethod
    def get_total_remaining(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        yearly_compounds = loan_terms['yearly_compounds']
        current_period = loan_terms['current_period']

        return LoanView.display_basic('Total Remaining',
            Loan.calc_total_remaining(
                rate, years, amount, yearly_compounds, current_period))


    # Charting --------------------------------------------------------
    @staticmethod
    def get_amortization(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        yearly_compounds = loan_terms['yearly_compounds']

        return LoanView.display_amortization(
            Loan.amortize_loan(rate, years, amount, yearly_compounds))
