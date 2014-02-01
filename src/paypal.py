import urllib
import urllib2
import urlparse

ENDPOINT_SANDBOX = "https://api-3t.sandbox.paypal.com/nvp"


class ExpressCheckout(object):

    def __init__(self, username, password, signature, sandbox=False):
        self.username = username
        self.password = password
        self.signature  = signature
        if sandbox:
            self.endpoint = ENDPOINT_SANDBOX

    def _post_data(self, url, data):
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


    def _validate_field(self, field, value):
        """ Validates the value given the field.
        field: String (amount, currency_id)
        value: String

        currency_id:
            Must be a valid one of those specified at the documentation:
            https://developer.paypal.com/docs/classic/api/currency_codes/ 

        amount:
            Regardless of the specified currency, the format must have
            a decimal point with exactly two digits to the right and an 
            optional thousands separator to the left, which must be a 
            comma.
        """

        CURRENCY_IDS = ["AUD", "BRL", "CAD", "CZK", "DKK", "EUR", "HKD",
            "HUF", "ILS", "JPY", "MYR", "MXN", "NOK", "NZD", "PHP", "PLN",
            "GBP", "RUB", "SGD", "SEK", "CHF", "TWD", "THB", "TRY", "USD"
        ] 

        if field == "amount":
            if "{0:.2f}".format(float(value)) == value:
                return True
            else:
                return False
        elif field == "currency_id":
            return True if value in CURRENCY_IDS else False
            

    def _set_express_checkout_request(self, amount, currency_id,return_url,
            cancel_url):
        """ Creates a proper request to be posted """
        if self._validate_field("amount", amount) and\
            self._validate_field("currency_id", currency_id):

            obj_for_request = {
                "METHOD": "SetExpressCheckout",
                "VERSION": "XX.0",
                "USER": self.username,
                "PWD": self.password,
                "SIGNATURE": self.signature,
                "PAYMENTREQUEST_0_AMT": amount,
                "PAYMENTREQUEST_0_CURRENCYCODE": currency_id, 
                "RETURNURL": return_url,
                "CANCELURL": cancel_url,
                "PAYMENTREQUEST_0_PAYMENTACTION": "Sale" 
            }

            key_value_request = urllib.urlencode(obj_for_request)

            # key_value_request = """
            #     METHOD=SetExpressCheckout
            #     VERSION=XX.0
            #     USER={username}
            #     PWD={password}
            #     SIGNATURE={signature}
            #     PAYMENTREQUEST_0_AMT={amount}
            #     PAYMENTREQUEST_0_CURRENCYCODE={currency_id}
            #     RETURNURL={return_url}
            #     CANCELURL={cancel_url}
            #     PAYMENTREQUEST_0_PAYMENTACTION=Sale
            # """.format(username=self.username, password=self.password,
            #     signature=self.signature, amount=amount,currency_id=currency_id,
            #     return_url=return_url, cancel_url=cancel_url)
            return key_value_request
        else:
            raise Exception("the amount field is not valid")

    def setExpressCheckout(self, amount, currency_id, return_url, cancel_url):
        """ Performs the setExpressCheckout request and returns the
            response in a python dict"""
        data = self._set_express_checkout_request(amount, currency_id, \
            return_url, cancel_url)
        return urlparse.parse_qs(self._post_data(self.endpoint, data))





def main():
    username = "ciro9758_api1.gmail.com"
    password = 1390922883
    signature = "AFcWxV21C7fd0v3bYYYRCpSSRl31AFdl6Gwn9pQHqzliaz6mNHjRfG.k"