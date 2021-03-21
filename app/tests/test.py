import requests
import unittest
import json


class APITest(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/"
    API_URl = f"{BASE_URL}/ProcessPayment"

    def test_successful_payment(self):
        # test with CheapPaymentGateway
        data = {"CreditCardNumber": "9221-4567-8911-3456", "CardHolder": "abc", "ExpirationDate": "2023/01",
                "Amount": 12, "SecurityCode": "123"}
        response = requests.post(self.API_URl, data=json.dumps(data))
        json_response = response.json()
        self.assertEqual(json_response['status_code'], 200)
        self.assertEqual(json_response['msg'], f"Payment of {data['Amount']} through CheapPaymentGateway is successful")

        # test with ExpensivePaymentGateway
        data['Amount'] = 21
        response = requests.post(self.API_URl, data=json.dumps(data))
        json_response = response.json()
        self.assertEqual(json_response['status_code'], 200)
        self.assertEqual(json_response['msg'], f"Payment of {data['Amount']} through ExpensivePaymentGateway is successful")

        # test with ExpensivePaymentGateway
        data['Amount'] = 600
        response = requests.post(self.API_URl, data=json.dumps(data))
        json_response = response.json()
        self.assertEqual(json_response['status_code'], 200)
        self.assertEqual(json_response['msg'],
                         f"Payment of {data['Amount']} through PremiumPaymentGateway is successful")

        # test with ExpensivePaymentGateway and without security code
        data['Amount'] = 600
        data.pop("SecurityCode")
        response = requests.post(self.API_URl, data=json.dumps(data))
        json_response = response.json()
        self.assertEqual(json_response['status_code'], 200)
        self.assertEqual(json_response['msg'],
                         f"Payment of {data['Amount']} through PremiumPaymentGateway is successful")

    def test_unsuccessful_payment(self):
        # test with invalid card details
        data = {"CardHolder": "abc", "ExpirationDate": "2023/01",
                "Amount": 12, "SecurityCode": "123"}
        response = requests.post(self.API_URl, data=json.dumps(data))
        json_response = response.json()
        self.assertEqual(json_response['status_code'], 400)
        self.assertEqual(json_response['msg'], "Invalid card details")

        # test with invalid credit card number
        data = {"CreditCardNumber": "922-4567-8911-3456", "CardHolder": "abc", "ExpirationDate": "2023/01",
                "Amount": 12, "SecurityCode": "123"}
        response = requests.post(self.API_URl, data=json.dumps(data))
        json_response = response.json()
        self.assertEqual(json_response['status_code'], 400)
        self.assertEqual(json_response['msg'], "Credit card number is not valid. It should contain 16 digits")

        # test with invalid card holder
        data = {"CreditCardNumber": "9221-4567-8911-3456", "CardHolder": 123, "ExpirationDate": "2023/01",
                "Amount": 12, "SecurityCode": "123"}
        response = requests.post(self.API_URl, data=json.dumps(data))
        json_response = response.json()
        self.assertEqual(json_response['status_code'], 400)
        self.assertEqual(json_response['msg'], "Card holder should be of string type")

        # test with invalid expiration date
        data = {"CreditCardNumber": "9221-4567-8911-3456", "CardHolder": "abc", "ExpirationDate": "2023/01/25",
                "Amount": 12, "SecurityCode": "123"}
        response = requests.post(self.API_URl, data=json.dumps(data))
        json_response = response.json()
        self.assertEqual(json_response['status_code'], 400)
        self.assertEqual(json_response['msg'], "Date is not correct it should be in this format: year/month e.g. 2021/12")

        # test with invalid amount
        data = {"CreditCardNumber": "9221-4567-8911-3456", "CardHolder": "abc", "ExpirationDate": "2023/01",
                "Amount": 0, "SecurityCode": "123"}
        response = requests.post(self.API_URl, data=json.dumps(data))
        json_response = response.json()
        self.assertEqual(json_response['status_code'], 400)
        self.assertEqual(json_response['msg'],
                         "Amount is not valid")

        # test with invalid amount
        response = requests.post(self.API_URl)
        json_response = response.json()
        self.assertEqual(json_response['status_code'], 400)
        self.assertEqual(json_response['msg'],
                         "There is no data in the request")


if __name__ == '__main__':
    unittest.main()
