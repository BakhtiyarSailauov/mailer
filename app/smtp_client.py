import os
import aiosmtplib

SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")


async def send_email(to: str, subject: str, message: str) -> bool:
    try:
        await aiosmtplib.send(
            message,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            username=SMTP_USER,
            password=SMTP_PASSWORD,
            sender=SMTP_USER,
            recipients=[to],
        )
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
