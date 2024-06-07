import os
import smtplib as s
from email.message import EmailMessage

# Define the SMTP server
SMTP_SERVER = 'smtp.gmail.com'
PORT = 587

# Define email credentials
email_address = ''
password = ''

# Define email content
subject = ""
body = """

"""

# Path to the image file you want to attach
attachment_path = r''

# Define recipient email addresses
recipients = ['']

# Create the email message
msg = EmailMessage()
msg['From'] = email_address
msg['To'] = ', '.join(recipients)
msg['Subject'] = subject
msg.set_content(body)

# Add the image attachment
try:
    with open(attachment_path, 'rb') as file:
        file_data = file.read()
        file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename=file_name)
except Exception as e:
    print(f"Failed to read the attachment: {e}")
    raise

try:
    # Connect to the SMTP server
    with s.SMTP(SMTP_SERVER, PORT) as smtp:
        smtp.ehlo()  # Identify ourselves to the SMTP server
        smtp.starttls()  # Start TLS encryption
        smtp.ehlo()  # Re-identify ourselves as an encrypted connection

        # Log in to the email account
        smtp.login(email_address, password)

        # Send the email
        smtp.send_message(msg)
        print("Mail sent successfully.")

except Exception as e:
    # Print an error message if the email fails to send
    print("Failed to send mail.")
    print(f"Error: {e}")
