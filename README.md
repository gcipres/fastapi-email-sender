# fastapi-mail-sender
Simple project to send emails

## Steps to run

Execuete `uvicorn src.main:app --reload --port 9000`

Next you will enter to the follow url to check the API documentation `http://127.0.0.0:9000/docs`

You need first excecute the next request:
```
Request: POST | /mail-sender/send
Body: {
  "email": "<your email here>",
  "text": "<your message body here>
}
```
*** Check the .env file into config folder to set a mail service variables and check permission in your email server, ej this for google (https://support.google.com/mail/answer/185833?hl=en-419) ***