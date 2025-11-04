from fastapi import FastAPI
from api import authtoken
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Daraja Access Token", "data": "Hello world"}




@app.get('/get_token')
def get_token():
    token_res = authtoken.get_auth_token()
    return {"message": "Daraja Access Token", "data": token_res}

