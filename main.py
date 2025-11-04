from fastapi import FastAPI
from api import authtoken

app = FastAPI()

@app.get("/")
def root():
    """Call the /get_token route and return the token."""
    token_response =  authtoken.get_token()
    return {"message": "Daraja Access Token", "data": token_response}



@app.get("/get_token")
def get_access_token():
    """Fetch OAuth access token from Safaricom Daraja API."""
    token_response = authtoken.get_token()
    return {"message": "Daraja Access Token", "data": token_response}
