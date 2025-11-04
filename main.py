from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Daraja Access Token", "data": "Hello world"}



