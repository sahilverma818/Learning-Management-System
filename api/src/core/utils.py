from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from jinja2 import Environment, FileSystemLoader
from src.core.config import settings
from src.core.logger import logger


def send_email(receiver, data, template_name, subject):
    try:
        env = Environment(loader=FileSystemLoader('static/templates'))
        template = env.get_template(template_name)

        html_content = template.render(data=data)

        message = MIMEMultipart()
        message["From"] = settings.EMAIL_ADDRESS
        message["To"] = receiver
        message["Subject"] = subject

        message.attach(MIMEText(html_content, "html"))

        server = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)
        server.starttls()
        server.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
        server.sendmail(settings.EMAIL_ADDRESS, receiver, message.as_string())
        server.quit()

        return True

    except Exception as e:
        logger.error(f"Failed to send email. Error: {e}")
        raise e