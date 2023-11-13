import smtplib
from email.mime.text import MIMEText
import json

# Sample JSON data
json_data = {'key': 'value', 'another_key': 42}

# Convert JSON to string
json_string = json.dumps(json_data, indent=2)

# Email configuration
sender_email = 'your_email@gmail.com'
receiver_email = 'recipient_email@example.com'
subject = 'JSON Data via Email'
body = json_string

# Email server configuration (for Gmail)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_email_password'

# Create the email message
message = MIMEText(body)
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Email sent successfully')
