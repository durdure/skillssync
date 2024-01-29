from flask_mail import Message
from app import mail
from app.config import Config

config = Config()



def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=config.MAIL_DEFAULT_SENDER
    )
    mail.send(msg)