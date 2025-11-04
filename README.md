# 🚀 Daraja 2.0 API — Beginner to Expert (Python + FastAPI)

This project is a complete implementation of Safaricom's Daraja API using Python and FastAPI, guiding you from beginner to expert in building, testing, and deploying M-Pesa integrations.

## 🌐 Live Demo

**Backend URL:** https://daraja-python-tutorial.fly.dev/

**Get Access Token:** https://daraja-python-tutorial.fly.dev/get_token

## 🧩 Features

- 🔐 Generate OAuth Access Tokens from Safaricom
- 💳 Simulate Customer-to-Business (C2B) and Business-to-Customer (B2C) payments
- 🧾 Handle Transaction Callbacks
- 📜 Organized FastAPI structure with clear endpoints
- 🐳 Dockerized setup for easy deployment
- ☁️ Ready to deploy on Fly.io

## ⚙️ Project Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/madegwa-kidii/daraja-python-tutorial.git
cd daraja-python-tutorial
```

### 2️⃣ Create and activate a virtual environment
```bash
# For Linux/Mac
python -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create a .env file
```env
CONSUMER_KEY=your_consumer_key
CONSUMER_SECRET=your_consumer_secret
SHORT_CODE=600XXX
PASS_KEY=your_pass_key
CALLBACK_URL=https://your-callback-url.com
```

## 🚀 Run the Application
```bash
uvicorn main:app --reload
```

Visit your app at: **http://127.0.0.1:8000**

## 🪙 Generate Access Token

You can easily generate a Safaricom Daraja Access Token using the `/get_token` endpoint.

### 🔹 Endpoint
```
GET /get_token
```

### 🔹 Description

Fetches an OAuth access token directly from the Safaricom Daraja API using your configured credentials.

### 🔹 Example Response
```json
{
  "message": "Daraja Access Token",
  "data": {
    "access_token": "YOUR_GENERATED_ACCESS_TOKEN",
    "expires_in": "3599"
  }
}
```

### 🔹 How to Use

1. Make sure your `.env` file contains valid credentials
2. Start the FastAPI app
3. Visit: http://127.0.0.1:8000/get_token
4. Copy the returned token and use it in your Daraja API requests

## 🧪 Example: Using the Access Token in Postman

1. Open Postman and set your request URL to:
```
   https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest
```

2. Under **Headers**, add:
```
   Authorization: Bearer <your-access-token>
   Content-Type: application/json
```

3. Send a valid request body as per Daraja documentation

## 🐳 Deploy on Fly.io

To deploy your project, use the included `Dockerfile` and `fly.toml`:
```bash
fly launch
fly deploy
```

Make sure your environment variables are set using:
```bash
fly secrets set CONSUMER_KEY=your_key CONSUMER_SECRET=your_secret
```

## 📁 Project Structure
```
daraja-python-tutorial/
│
├── api/
│   ├── authtoken.py
│   ├── transactions.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
├── Dockerfile
├── fly.toml
├── .gitignore
└── README.md
```

## 🧑‍💻 Author

**Madegwa Kiddi**

💼 GitHub: [@madegwa-kidii](https://github.com/madegwa-kidii)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/madegwa-kidii/daraja-python-tutorial/issues).
