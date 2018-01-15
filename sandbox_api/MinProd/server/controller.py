from MinProd import app
from MinProd.server.controllers.ping import PingController
from MinProd.server.controllers.data import DataController
from MinProd.server.controllers.error import ErrorController
from MinProd.server.controllers.security import SecurityController

from MinProd.server.controllers.loan import LoanController
from MinProd.server.controllers.mortgage import MortgageController


# raise ValueError('Error Test')
# Not using this right now. Might use it for composed clsses later

class PingController(PingController):
    pass

class DataController(DataController):
    pass

class ErrorController(ErrorController):
    pass

class SecurityController(SecurityController):
    pass

class LoanController(LoanController):
    pass

class MortgageController(MortgageController):
    pass
