from datetime import datetime


class ErrorController():
  @staticmethod
  def handle_errors(e):
    #subject = 'MINPROD API ERROR ' + str(datetime.now())
    #EmailController.send_email(subject, str(e))
    return 500
