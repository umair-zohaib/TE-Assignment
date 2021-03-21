import re
from decimal import Decimal
from datetime import datetime


class Card:
    def __init__(self):
        self.CreditCardNumber = None
        self.CardHolder = None
        self.ExpirationDate = None
        self.SecurityCode = None
        self.Amount = None

    @staticmethod
    def validate_card(card):
        if re.search(r"^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$", card):
            return True
        return False

    @staticmethod
    def get_start_date_of_month():
        today = datetime.today()
        date = datetime(today.year, today.month, 1).date()
        return date

    def verify_input(self, **kwargs):
        """
        -CreditCardNumber: (mandatory, string, it should be a valid credit card number)
        -CardHolder: (mandatory, string)
        -ExpirationDate: (mandatory, DateTime, it cannot be in the past)
        -SecurityCode: (optional, string, 3 digits)
        -Amount: (mandatory decimal, positive amount)
        """
        required_card_values = {"CreditCardNumber", "CardHolder", "ExpirationDate", "Amount"}
        if required_card_values.intersection(kwargs.keys()) != required_card_values:
            msg = "Invalid card details"
            return False, msg

        credit_card_number = kwargs.get("CreditCardNumber")
        card_holder = kwargs.get("CardHolder")
        expiration_date = kwargs.get("ExpirationDate")
        security_code = kwargs.get("SecurityCode")
        amount = kwargs.get("Amount")

        if not (type(credit_card_number) == str and self.validate_card(credit_card_number)):
            msg = "Credit card number is not valid. It should contain 16 digits"
            return False, msg

        if not type(card_holder) == str:
            msg = "Card holder should be of string type"
            return False, msg

        if security_code:
            if not (type(security_code) == str and len(security_code) == 3) or not security_code.isdigit():
                msg = "Security code is not correct"
                return False, msg

        try:
            msg = "Date is not correct it should be in this format: year/month e.g. 2021/12"
            current_date = self.get_start_date_of_month()
            input_date = datetime.strptime(expiration_date, "%Y/%m").date()

            if not input_date > current_date:
                return False, msg

            msg = "Amount is not valid"
            if not Decimal(amount) > 0:
                return False, msg
        except:
            return False, msg

        self.CreditCardNumber = credit_card_number
        self.CardHolder = card_holder
        self.SecurityCode = security_code
        self.ExpirationDate = expiration_date
        self.Amount = amount

        msg = "User Input is verified"
        return True, msg
