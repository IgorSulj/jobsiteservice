import os
import smtplib
from email.message import EmailMessage

from .docxtable import DocxTable
from env import DEBUG, HOME_EMAIL, PASSWORD, RESERVE_EMAIL
from models import WorkBlankModel

DOCX_FORMAT = ('application',
               'vnd.openxmlformats-officedocument.wordprocessingml.document')


def generate_message(docx_table: DocxTable, target: str, subject='Анкета', text='') -> EmailMessage:
    msg = EmailMessage()
    msg['Subject'] = 'Заполненная анкета'
    msg['From'] = os.getenv('HOME_EMAIL')
    msg['To'] = target
    msg.set_content(text)
    msg.add_attachment(docx_table.as_docx_stream().read(),
                       maintype=DOCX_FORMAT[0], subtype=DOCX_FORMAT[1], filename='Анкета.docx')
    return msg


class EmailHandler:
    @classmethod
    def send_email(cls, email: EmailMessage) -> None:
        raise NotImplementedError()


class SmtpHandlerMock(EmailHandler):
    @classmethod
    def send_email(cls, email: EmailMessage):
        print("Sending email... (mock)")


MainHandler = SmtpHandlerMock

if not DEBUG:
    client = smtplib.SMTP('mail.rabotavsem.by', 587)
    client.starttls()
    client.login(HOME_EMAIL, PASSWORD)

    class SmtpHandler(EmailHandler):
        @classmethod
        def send_email(cls, email: EmailMessage):
            client.send_message(email)

    MainHandler = SmtpHandler


def send_blank(
        blank: WorkBlankModel,
        email_handler: type[EmailHandler] = MainHandler):

    docx_table = DocxTable.from_blank(blank)
    email_handler.send_email(
        generate_message(
            docx_table, 
            target=blank.contacts.email, 
            text='Это ваша копия анкеты. Она также была автоматически отправлена нам.'
        )
    )
    email_handler.send_email(
        generate_message(
            docx_table, 
            target=RESERVE_EMAIL,
            subject=f'Анкета от {blank.personal.russian_name}',
        )
    )
