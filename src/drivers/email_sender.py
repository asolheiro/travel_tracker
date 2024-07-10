import smtplib
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_addrs, body):
    with open("ethreal_email/output_formatted.json", "r") as file:
        dados = json.load(file)

    from_addrs = dados['user']
    user = dados['user']
    password = dados['pass']

    print(from_addrs, user, password)
    msg = MIMEMultipart()

    msg["from"] = "viagens_confirmar@email.com"
    msg["to"] = ", ".join(to_addrs)
    msg["Subject"] = "Confirmação de viagem!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(user, password)

    text = msg.as_string()
    for email in to_addrs:
        server.sendmail(from_addrs, email, text)

    server.quit()

