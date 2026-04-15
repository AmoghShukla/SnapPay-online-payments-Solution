from fastapi import FastAPI

app = FastAPI(title="SnapPay : Your Payments Solution Partner")

@app.get('/')
def home():
    return {
        'message' : 'Your Payments Application is up and running!!'
    }