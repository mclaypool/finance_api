from flask import jsonify

from MinProd import app
from MinProd.server.views.base import BaseView


class LoanView(BaseView):
    @staticmethod
    def display_amortization(amort_sched):
        # dict is the follow: {period, [pmt, ipmt, ppmt, balance]}
        return jsonify(amort_sched)
