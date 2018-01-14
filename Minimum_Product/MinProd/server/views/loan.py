from flask import jsonify


class LoanView():
    # Payments --------------------------------------------------------
    @staticmethod
    def display_monthly_payment(payment):
        return jsonify({ 'Monthly Payment': str(payment)})


    # Principle -------------------------------------------------------



    # Interest --------------------------------------------------------



    # Charting --------------------------------------------------------

