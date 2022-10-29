import smtplib
from os import getenv
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email_with_file(sender: str, receiver_list: list, filename_list: list):
    """Attaches files base on the filename list and 
    sends an email to the receivers"""
    if (type(receiver_list) is not list or 
    type(filename_list) is not list):
        raise TypeError("Arguments must be in a list")

    password = getenv('PY_PW')
    if password is None:
        raise RuntimeError("Environment Variable not configured")
    subject = "Team Stats in PDF"
    content = "Hey there!\nCheck out these stats..."
    body = MIMEText(content, 'plain')

    message = MIMEMultipart()
    message["From"] = sender
    message["Subject"] = subject
    message.attach(body)

    for file in filename_list:
        with open(file, 'r') as f:
            attachment = MIMEApplication(f.read(), Name=basename(file))
            attachment['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(file))
        message.attach(attachment)
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', port=465)
    server.login(sender, password)
    server.send_message(message, from_addr=sender, to_addrs=receiver_list)

