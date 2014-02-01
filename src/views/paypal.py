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
            
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(resposta)