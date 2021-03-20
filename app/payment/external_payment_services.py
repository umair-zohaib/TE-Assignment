class BasePaymentGateway:
    def __init__(self, retry=0):
        self.gateway = None
        self.retry = retry

    def __repr__(self):
        return "<BasePaymentGateway>"

    @staticmethod
    def authenticate(details=None):
        if details is not None:
            return True
        return False

    def connect(self, gateway=None, details=None):
        if gateway is not None:
            if self.authenticate(details):
                return True, "You have been connected to the gateway"
        return False, "You have not been connected to the gateway"

    def pay(self, amount, user_details=None, gateway=None):
        if gateway is None:
            gateway = self.gateway
        while self.retry + 1 > 0:
            status, msg = self.connect(gateway, user_details)
            if status:
                # print(f"payment of {amount} in gateway {self.gateway} is successful")
                msg = f"Payment of {amount} through {self.gateway} is successful"
                return True, msg
            self.retry -= 1
        return False, msg


class PremiumPaymentGateway(BasePaymentGateway):
    def __init__(self, retry=3):
        super(PremiumPaymentGateway, self).__init__(retry)
        self.gateway = "PremiumPaymentGateway"

    def __repr__(self):
        return "<PremiumPaymentGateway>"


class ExpensivePaymentGateway(BasePaymentGateway):
    def __init__(self, retry=1):
        super(ExpensivePaymentGateway, self).__init__(retry)
        self.gateway = "ExpensivePaymentGateway"

    def __repr__(self):
        return "<ExpensivePaymentGateway>"


class CheapPaymentGateway(BasePaymentGateway):
    def __init__(self, retry=0):
        super(CheapPaymentGateway, self).__init__(retry)
        self.gateway = "CheapPaymentGateway"

    def __repr__(self):
        return "<CheapPaymentGateway>"


class ExternalPaymentService:
    def __init__(self, amount, card_details=None):
        self.amount = amount
        self.card_details = card_details

    def make_payment(self):
        try:
            if self.amount <= 20:
                payment_method = CheapPaymentGateway()
            elif 20 < self.amount < 500:
                payment_method = ExpensivePaymentGateway()
            elif self.amount >= 500:
                payment_method = PremiumPaymentGateway()
            else:
                return False, f"Amount: {self.amount} is not valid"

            status, msg = payment_method.pay(self.amount, self.card_details)
            return status, msg
        except:
            return False, "Error occurred while making payment"
