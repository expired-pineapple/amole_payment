import requests

class AmoleAPI:
    """Amole API class"""
    def __init__(self, base_url, username, password, APISignaure):
        """Initialize Amole API class
        Args:
            base_url (str): Base URL of Amole API
            username (str): Username given by Amole
            password (str): Password given by Amole
            APISignaure (str): API Signature given by Amole
        """
        base_url="http://uatc.api.myamole.com:8075/amole/pay"
        header = {"Content-Type": "application/x-www-form-urlencoded",
                    "HDR_Signature": APISignaure,
                    "HDR_Username": username,
                    "HDR_Password": password,
                }
        self.base_url = base_url
        self.header = header  
        self.transaction_id = 1


class Payment(AmoleAPI):
    
    def authorize_payment(self, card_number, merchant_id, *args, **kwargs):
        """This method is used to authorize a payment
            Args:
                card_number (str): The card number to be authorized
                merchant_id (str): The merchant id
            Returns:
                response (dict): The response from the API
        """
        data = {
                "BODY_CardNumber": card_number,
                "BODY_PaymentAction": "09",
                "BODY_AmoleMerchantID": merchant_id
            }
        response = requests.post(self.base_url, data=data, headers=self.header)
        return response.json()


    def pay(self, amount, card_number,otp,merchant_id,expiration_date,*args, **kwargs ):
        # if not otp:
        #     authorize_payment = self.authorize_payment(card_number, merchant_id)
        #     if authorize_payment[0]["MSG_ErrorCode"] != "00001":
                
        #         return authorize_payment

        """This method is used to make a payment
            Args:
                amount (str): The amount to be paid
                card_number (str): The card number to be paid
                otp (str): The otp to be used for the payment
                merchant_id (str): The merchant id
            Returns:
                response (dict): The response from the API
        """
        
        data = {
                    "BODY_CardNumber": card_number,
                    "BODY_ExpirationDate": expiration_date,
                    "BODY_PIN": otp,
                    "BODY_PaymentAction": "01",
                    "BODY_AmountX": amount,
                    "BODY_AmoleMerchantID": merchant_id
                }
        response = requests.post(self.base_url, data=data, headers=self.header)
        return response.json()
    
    def send_request(self, params, *args, **kwargs):
        """This method is used to send a request to the API
            Args:
                params (dict): The parameters to be sent to the API
            Returns:
                response (dict): The response from the API
        """
        response = requests.post(self.base_url, data=params, headers=self.header)
        return response.json()


    

