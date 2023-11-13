import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import json


def sendmail(json_data):
    # Email configuration
    sender_email = 'autocoiltest@gmail.com'
    receiver_email = 'autocoiltest@gmail.com'
    subject = 'JSON Data via Email'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'autocoiltest@gmail.com'
    smtp_password = 'secret'

    # Convert JSON to string
    json_string = json.dumps(json_data, indent=2)

    # Create the email message
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    # Attach the JSON data as a file
    attachment = MIMEApplication(json_string, _subtype='json')
    attachment.add_header('Content-Disposition', 'attachment', filename='data.json')
    message.attach(attachment)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print('Email sent successfully')

