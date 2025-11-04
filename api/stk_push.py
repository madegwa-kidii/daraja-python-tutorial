import base64
import datetime
import requests
from api import authtoken

# Safaricom sandbox endpoint
STK_PUSH_URL = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

# Credentials and configuration
BUSINESS_SHORTCODE = "174379"
PASSKEY = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
CALLBACK_URL = "https://1df0737dee7c.ngrok-free.app/callback"


def generate_password():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    data_to_encode = BUSINESS_SHORTCODE + PASSKEY + timestamp
    encoded = base64.b64encode(data_to_encode.encode()).decode("utf-8")
    return encoded, timestamp


def initiate():
    try:
        # 1️⃣ Get access token
        token_data = authtoken.get_auth_token()
        if "access_token" not in token_data:
            return {"error": "Failed to get access token", "data": token_data}

        access_token = token_data["access_token"]

        # 2️⃣ Generate password and timestamp
        password, timestamp = generate_password()

        # 3️⃣ Create STK push payload
        payload = {
            "BusinessShortCode": BUSINESS_SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": 1,
            "PartyA": "254708374149",
            "PartyB": BUSINESS_SHORTCODE,
            "PhoneNumber": "254708374149",
            "CallBackURL": CALLBACK_URL,
            "AccountReference": "CompanyXLTD",
            "TransactionDesc": "Payment of X"
        }

        # 4️⃣ Send request
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        response = requests.post(STK_PUSH_URL, json=payload, headers=headers)

        # 5️⃣ Return response
        if response.status_code == 200:
            return response.json()

        return {
            "error": response.status_code,
            "message": response.text
        }

    except Exception as e:
        return {"error": str(e)}


def callback(data=None):
    """Handle Daraja callback (Safaricom -> your app)."""
    try:
        if not data:
            return {"message": "No callback data received"}
        return {"message": "Callback received", "data": data}
    except Exception as e:
        return {"error": str(e)}
