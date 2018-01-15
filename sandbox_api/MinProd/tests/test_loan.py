import unittest

from flask import Flask

app = Flask(__name__) 

from MinProd.server.models.loan import Loan


class TestLoan(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.assertEqual(app.debug, False)
 
    def tearDown(self):
        pass

    def test_calc_monthly_payment(self):
            self.assertEqual(184.17, 0)



#curl -i -X GET -H "Content-Type: application/json" 
#-d '{"loan_terms": 
#{"yearly_rate":"0.04","length_years":"5", "loan_amount":"10000"}}' 
#http://127.0.0.1:5000/loan/monthlypayment


if __name__ == '__main__':
    unittest.main()
