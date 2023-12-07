import os
import smtplib
from email.message import EmailMessage

from docxtable import DocxTable
from env import DEBUG, HOME_EMAIL, PASSWORD, RESERVE_EMAIL
from models import WorkBlankModel

DOCX_FORMAT = ('application',
               'vnd.openxmlformats-officedocument.wordprocessingml.document')


def generate_message(docx_table: DocxTable, target: str) -> EmailMessage:
    msg = EmailMessage()
    msg['From'] = os.getenv('HOME_EMAIL')
    msg['To'] = docx_table
    msg.add_attachment(docx_table.as_docx_stream().read(),
                       maintype=DOCX_FORMAT[0], subtype=DOCX_FORMAT[1])
    return msg


class EmailHandler:
    @classmethod
    def send_email(cls, email: EmailMessage) -> None:
        raise NotImplementedError()


class SmtpHandlerMock(EmailHandler):  # type: ignore
    @classmethod
    def send_email(cls, email: EmailMessage):
        print(email)


MainHandler = SmtpHandlerMock

if not DEBUG:
    client = smtplib.SMTP('mail.rabotavsem.by', 25)
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
        generate_message(docx_table, blank.contacts.email)
    )
    email_handler.send_email(
        generate_message(docx_table, RESERVE_EMAIL)
    )
