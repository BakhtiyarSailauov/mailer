from pydantic import BaseModel, EmailStr


class EmailPayload(BaseModel):
    to: EmailStr
    subject: str
    message: str
