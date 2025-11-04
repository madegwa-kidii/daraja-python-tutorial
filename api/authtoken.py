import base64
import requests

# Replace these with your actual Daraja app credentials
CONSUMER_KEY = "cCwfVNmUvxQSwZJ5kBcoOuO1BPiUDDeC03bv7r2zgHOQjr0K"
CONSUMER_SECRET = "ODYemIpORm4GgfIfLFrPdnNB354ihnssfaAG3sSnhiGjO4cSz0rJj10qTKe14OGm"

AUTH_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

def get_token():
    try:
        # get credentials
        credentials = f"{CONSUMER_KEY}:{CONSUMER_SECRET}"

        # encode credentials
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

        print("encoded_credentials: ", encoded_credentials)

        # send the get request
        response = requests.get(AUTH_URL, headers={"Authorization": "Basic " + encoded_credentials})

        if response.status_code == 200:
            return response.json()

        else:
            return {
                "error_code": str(response.status_code),
                "error_msg": str(response.text)

            }


    except Exception as e:
        return {"error": str(e)}
