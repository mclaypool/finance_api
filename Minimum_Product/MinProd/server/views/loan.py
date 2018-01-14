from flask import jsonify

from MinProd import app
from MinProd.server.views.base import BaseView


class LoanView(BaseView):
    @staticmethod
    def display_amortization_schedule():
        return None
