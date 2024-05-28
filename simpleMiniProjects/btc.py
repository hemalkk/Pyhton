import requests
from bs4 import BeautifulSoup as bs
import smtplib as s

# Define the URL of the web page
url = "https://www.coinspot.com.au/buy/btc"

# Send a GET request to the URL
r = requests.get(url)

# Parse the HTML content of the page
soup = bs(r.content, "html.parser")

# Find the element containing the buy price
buyPrice = soup.find('span', {'class': 'title'})

# Check if the price element was found and get the price text
if buyPrice:
    price_text = buyPrice.text.strip()
    print(price_text)
else:
    price_text = "Price not found"
    print(price_text)

# Define SMTP server details
SMTP_SERVER = 'smtp.gmail.com'
PORT = 587

# Define email credentials (fill in your details)
email_address = 'your_email@gmail.com'
password = 'your_password'

# Define email content
subject = "BTC price"
body = f"The current BTC buy value is {price_text}"
message = f"Subject: {subject}\n\n{body}"

# Define recipient email addresses (fill in recipient details)
recipients = ['recipient_email@example.com']

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
        print("Mail sent successfully.")

except Exception as e:
    # Print an error message if the email fails to send
    print("Failed to send mail.")
    print(f"Error: {e}")
