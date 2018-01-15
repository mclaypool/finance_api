from MinProd import app
from MinProd.server.models.loan import Loan
from MinProd.server.views.loan import LoanView


class LoanController():
    # Payments --------------------------------------------------------
    @staticmethod
    def get_monthly_payment(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']

        return LoanView.display_basic('Monthly Payment', 
            Loan.calc_monthly_payment(rate, years, amount))


    @staticmethod
    def get_payment_ppart():
        return LoanView.display_basic('Principle Part', 
            Loan.calc_payment_ppart())


    @staticmethod
    def get_payment_ipart():
        return LoanView.display_basic('Interest Part',
            Loan.calc_payment_ipart())


    # Principle -------------------------------------------------------
    @staticmethod
    def get_principle_paid():
        return LoanView.display_basic('Principle Paid',
            Loan.calc_principle_paid())


    @staticmethod
    def get_principle_remaining():
        return LoanView.display_basic('Principle Remaining',
            Loan.calc_principle_remaining())


    # Interest --------------------------------------------------------
    @staticmethod
    def get_total_interest(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']

        return LoanView.display_basic('Total Interest',
            Loan.calc_total_interest(rate, years, amount))


    @staticmethod
    def get_interest_paid():
        return LoanView.display_basic('Interest Paid',
            Loan.calc_interest_paid())


    @staticmethod
    def get_interest_remaining():
        return LoanView.display_basic('Interest Remaining',
            Loan.calc_interest_remaining())

    # Totals --------------------------------------------------------
    @staticmethod
    def get_total_cost(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']

        return LoanView.display_basic('Total Cost',
            Loan.calc_total_cost(rate, years, amount))


    @staticmethod
    def get_total_remaining(loan_terms):
        rate = loan_terms['apr']
        years = loan_terms['years']
        amount = loan_terms['amount']
        current_period = loan_terms['current_period']

        return LoanView.display_basic('Total Remaining',
            Loan.calc_total_remaining(
                rate, years, amount, current_period))


    # Charting --------------------------------------------------------
    @staticmethod
    def get_amortization_schedule():
        return LoanView.display_amortization_schedule(
            Loan.calc_amortization_schedule())
