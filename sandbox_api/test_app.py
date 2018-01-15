import unittest

from MinProd.server.models.loan import Loan


class TestLoan(unittest.TestCase):
    def test_calc_monthly_payment(self):
        result = Loan.calc_monthly_payment(0.04, 5, 10000)
        self.assertEqual(result, 184.17)

    def test_calc_total_interest(self):
        result = Loan.calc_total_interest(0.04, 5, 10000)
        self.assertEqual(result, 1049.91)

    def test_calc_total_cost(self):
        result = Loan.calc_total_cost(0.04, 5, 10000)
        self.assertEqual(result, 11049.91)

    def test_calc_total_remaining(self):
        result = Loan.calc_total_remaining(0.04, 5, 10000, 59)
        self.assertEqual(result, 184.16)


if __name__ == '__main__':
    unittest.main()
