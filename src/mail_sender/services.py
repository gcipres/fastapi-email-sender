import os
from dotenv import load_dotenv
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr

load_dotenv('config/.env')

conf = ConnectionConfig(
        MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
        MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
        MAIL_FROM=os.getenv('MAIL_FROM'),
        MAIL_PORT=int(os.getenv('MAIL_PORT')),
        MAIL_SERVER=os.getenv('MAIL_SERVER'),
        MAIL_FROM_NAME=os.getenv('MAIL_FROM_NAME'),
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True
    )

async def send_support_mail(email: str, message: str):
    subject = "Hi buddy!"

    body = f"""
        <div style='width: 60%; margin: auto;'>
            <p>This is a message:</p>
            <p><i>{message}</i></p>
        </div>
    """

    email_to: EmailStr = email
    await send_mail(email_to, subject, body)

async def send_mail(email_to: EmailStr, subject: str, message_body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=message_body,
        subtype=MessageType.html,
    )
    
    fm = FastMail(conf)
    await fm.send_message(message)