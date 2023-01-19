import logging
from fastapi import APIRouter, status
from src.mail_sender import services
from src.mail_sender.schemas import Message

router = APIRouter()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s -%(name)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

@router.post("/mail-sender/send", status_code=status.HTTP_202_ACCEPTED)
async def support(message: Message) -> None:
    logger.info(f"[send email message] -> user: {message.email}")
    await services.send_support_mail(message.email, message.text)