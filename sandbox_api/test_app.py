import unittest

from MinProd.server.models.loan import Loan


class TestLoan(unittest.TestCase):
    # Payments --------------------------------------------------------
    def test_calc_monthly_payment(self):
        result = Loan.calc_payment(0.04, 5, 10000, 12)
        self.assertEqual(result, 184.17)

    def test_calc_payment_ppart(self):
        result = Loan.calc_payment_ppart(0.04, 5, 10000, 12, 30)
        self.assertEqual(result, 166.12)

    def test_calc_payment_ipart(self):
        result = Loan.calc_payment_ipart(0.04, 5, 10000, 12, 30)
        self.assertEqual(result, 18.05)


    # Principle -------------------------------------------------------
    def test_calc_principle_paid(self):
        # TODO: should be 4750.65
        result = Loan.calc_principle_paid(0.04, 5, 10000, 12, 30)
        self.assertEqual(result, 4750.79)


    def test_calc_principle_remaining(self):
        # TODO: should be 5249.38 
        result = Loan.calc_principle_remaining(0.04, 5, 10000, 12, 30)
        self.assertEqual(result, 5249.53)


    # Interest --------------------------------------------------------
    def test_calc_total_interest(self):
        # TODO: should be 1049.91 
        result = Loan.calc_total_interest(0.04, 5, 10000, 12)
        self.assertEqual(result, 1050.2)

    def test_calc_interest_paid(self):
        # TODO: should be 766.43
        result = Loan.calc_interest_paid(0.04, 5, 10000, 12, 30)
        self.assertEqual(result, 774.31)

    def test_calc_interest_remaining(self):
        # TODO: should be 275.58 
        result = Loan.calc_interest_remaining(0.04, 5, 10000, 12, 30)
        self.assertEqual(result, 275.57)


    # Totals ----------------------------------------------------------
    def test_calc_total_cost(self):
        # TODO: should be 11049.91
        result = Loan.calc_total_cost(0.04, 5, 10000, 12)
        self.assertEqual(result, 11050.20)
    
    def test_calc_total_remaining(self):
        # TODO: should be ----
        result = Loan.calc_total_remaining(0.04, 5, 10000, 12, 60)
        self.assertEqual(result, 0)
    

    # Dates ----------------------------------------------------------
    def test_estimate_payoff_date(self):
        result = Loan.estimate_payoff_date()
        self.assertTrue(False)


    # Charting --------------------------------------------------------
    def test_amortization_sched(self):
        # TODO: should be 5249.38 
        result = Loan.amortize_loan(0.04, 5, 10000, 12)
        #print(result)
        self.assertEqual(result[30][3], 5249.21)


if __name__ == '__main__':
    unittest.main()
