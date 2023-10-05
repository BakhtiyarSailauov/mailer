from fastapi import FastAPI, HTTPException, Depends
from models import EmailPayload
from smtp_client import send_email

app = FastAPI()


@app.post("/send_email")
async def send_email_endpoint(email_payload: EmailPayload):
    result = await send_email(email_payload.to, email_payload.subject, email_payload.message)
    if not result:
        raise HTTPException(status_code=400, detail="Email was not sent")
    return {"message": "Email sent successfully"}

