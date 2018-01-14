from MinProd import app
from MinProd.server.views.ping import PingView


class PingController():
    @staticmethod
    def get_ping_json():
        return PingView.display_response_json();
