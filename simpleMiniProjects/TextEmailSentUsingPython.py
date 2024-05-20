import smtplib as s

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
message = "Subject: {}\n\n{}".format(subject, body)

# Define recipient email addresses
recipients = ['']

try:
    # Connect to the SMTP server
    with s.SMTP(SMTP_SERVER, PORT) as smtp:
        smtp.ehlo()  # Identify ourselves to the SMTP server
        smtp.starttls()  # Start TLS encryption
        smtp.ehlo()  # Re-identify ourselves as an encrypted connection

        # Log in to the email account
        smtp.login(email_address, password)

        # Send the email
        smtp.sendmail(email_address, recipients, message)
        print("Mail Send Successfully.")

except Exception as e:
    # Print an error message if the email fails to send
    print("Failed to send mail.")
    print(f"Error: {e}")
