import base64
import requests

AUTH_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

CONSUMER_KEY = "reJjt6xnyvZdACLrlVvtI8GjCuUcIT5zWyq2xm5GzU4Np1nb"
CONSUMER_SECRET = "AvH0jMC0pLNnCekwUCfvG0ltXJ1kyZ1GzEA724H0KY9wnWKPU6QqC6h250FDxn5r"


def get_auth_token():
    try:
        credentials = f"{CONSUMER_KEY}:{CONSUMER_SECRET}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        headers = {"Authorization": f"Basic {encoded_credentials}"}
        response = requests.get(AUTH_URL, headers=headers)

        if response.status_code == 200:
            return response.json()

        return {
            "error": response.status_code,
            "message": response.text
        }
    except Exception as e:
        return {"error": str(e)}
