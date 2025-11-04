from fastapi import FastAPI, Request
from api import authtoken, stk_push

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Daraja Integration", "data": "Hello world"}


@app.get("/get_token")
def get_token():
    """Fetch OAuth access token from Safaricom Daraja API."""
    token_res = authtoken.get_auth_token()
    return {"message": "Daraja Access Token", "data": token_res}


@app.post("/stk_push")
def initiate_stk():
    """Trigger STK Push payment request."""
    stk_push_res = stk_push.initiate()
    return {"message": "STK Push initiated", "data": stk_push_res}


@app.post("/callback")
async def callback(request: Request):
    """Receive M-Pesa STK push callback."""
    data = await request.json()
    stk_callback_res = stk_push.callback(data)
    print('callback: ',stk_callback_res )

    return stk_callback_res
