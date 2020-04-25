import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path("index.html").read_text())

email = EmailMessage()
email['from'] = "Your_name"
email['to'] = "Senders_email_address"
email['subject'] = "Did you got your closure?"
email.set_content(html.substitute({name: "TinTin"}))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("your_email_address.com" ,"your_password")
    smtp.send_message(email)
    print("all done")
