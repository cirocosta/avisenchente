import webapp2
import settings
import json

from utils import ec_paypal

ec = ec_paypal.ExpressCheckout(settings.PP_USER,
        settings.PP_PASSWORD, settings.PP_SIGNATURE)


class PayPalSEC(webapp2.RequestHandler):

    def post(self):
        amount = self.request.get("amount")
        currency_id = self.request.get("currency_id")
        return_url = self.request.get("return_url")
        cancel_url = self.request.get("cancel_url")
        
        response = ec.setExpressCheckout(amount, currency_id, return_url, 
            cancel_url)
        print response
        if response['ACK'] == ['Success']:
            token = response['TOKEN']
            resposta = json.dumps({
                "success":True, 
                "data": {
                    "token": token[0]
                    }
                })
        else:
            resposta = json.dumps({"success": False})

        print resposta
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(resposta)


class PayPalGECD(webapp2.RequestHandler):

    def get(self):
        token = self.request.GET['token']
        payer_id = self.request.GET['PayerID']

        response = ec.getExpressCheckoutDetails(token)
        if response['ACK'] == ['Success']:
            pass
        resposta = json.dumps(response)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(resposta)


class PayPalIPN(webapp2.RequestHandler):

    def post(self):
        self.response.out.write("")
        response_verify = post_data("https://www.paypal.com/cgi-bin/webscr?cmd=_notify-validate",
            self.request.body())
        print response_verify
        

def post_data(self, url, data):
    """ Posts data to a given url

        params:
            url: a string containing the url
            data: a string or a dict containing data
                if string, must be urlencoded
    """
    if type(data) == dict:
        data = urllib.urlencode(data)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    return response.read()
