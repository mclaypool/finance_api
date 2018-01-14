from MinProd import app
from MinProd.server.models.loan import Loan
from MinProd.server.views.loan import LoanView


class LoanController():
    # Payments --------------------------------------------------------
    @staticmethod
    def calc_monthly_payment(yearly_rate, length_years, loan_amount):
        # pmt = (r * PV) / (1 - (1 + r)^-n)
        period_rate = float(yearly_rate) / 12
        periods = int(length_years) * 12
        pv = float(loan_amount)

        payment = period_rate * pv / (1 - (1 + period_rate) ** -periods)
        payment = round(payment, 2)

        return LoanView.display_monthly_payment(payment)


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


    # Charting --------------------------------------------------------
    @staticmethod
    def get_amortization_schedule():
        return None
