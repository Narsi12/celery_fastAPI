from fastapi import FastAPI 
from task import send_email

app = FastAPI()

@app.post("/send_email")
def send_email_api(receiver_email: str, subject: str, body: str):
    send_email.delay( receiver_email, subject, body)
    return {"message": "Email will be sent shortly."}
