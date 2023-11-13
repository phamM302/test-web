import imaplib
import email
from email.header import decode_header
import json

# IMAP server settings
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993
EMAIL_ADDRESS = 'autocoiltest@gmail.com'
EMAIL_PASSWORD = 'secret'

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

# Login to the email account
mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

# Select the mailbox you want to read emails from (e.g., 'inbox')
mail.select('inbox')

# Search for all emails in the mailbox
status, messages = mail.search(None, 'ALL')
mail_ids = messages[0].split()

# Iterate through the email IDs
for mail_id in mail_ids:
    # Fetch the email by ID
    status, msg_data = mail.fetch(mail_id, '(RFC822)')
    raw_email = msg_data[0][1]

    # Parse the raw email content
    msg = email.message_from_bytes(raw_email)

    # Check if the email has attachments
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            # Check if the attachment is a JSON file
            filename = part.get_filename()
            if filename.endswith('.json'):
                # Decode the JSON data and load it into a Python object
                json_data = json.loads(part.get_payload(decode=True).decode('utf-8'))

                # Now 'json_data' is a Python object containing the parsed JSON content
                print('Parsed JSON Data:')
                print(json_data)

                # Delete the email
                mail.store(mail_id, '+FLAGS', '(\Deleted)')
                mail.expunge()
                print(f'Email with ID {mail_id} deleted successfully')
    print('read')

# Logout and close the connection

mail.logout()
