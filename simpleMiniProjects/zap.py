# Import the BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Specify the path to the OWASP ZAP report
report_file = 'C:/Users/HK/Downloads/2024-10-04-ZAP-Report-.html'

# Open and read the HTML report
with open(report_file, 'r', encoding='utf-8') as file:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(file, 'html.parser')

# Find all alert items in the report
# We look for <li> elements whose id starts with 'alerts--risk'
alerts = soup.find_all('li', id=lambda x: x and x.startswith('alerts--risk'))

# Open a new file to save the parsed alerts
with open('parsed_alerts.txt', 'w', encoding='utf-8') as output_file:
    # Loop through each alert found
    for alert in alerts:
        # Extract risk level from the span with class 'risk-level'
        risk = alert.find('span', class_='risk-level').text.strip()

        # Extract confidence level from the span with class 'confidence-level'
        confidence = alert.find('span', class_='confidence-level').text.strip()

        # Extract the alert title from the h5 tag
        title = alert.find('h5').text.strip()

        # Extract the description if available
        # Find the <tr> element that contains 'Alert description' in its row
        description_tag = alert.find('tr', scope='row', string='Alert description')
        
        # If the description tag is found, get the text from the next <td>, else set to 'No description'
        description = description_tag.find_next('td').text.strip() if description_tag else 'No description'

        # Write the extracted information to the output file
        output_file.write(f'Title: {title}\n')
        output_file.write(f'Risk: {risk}\n')
        output_file.write(f'Confidence: {confidence}\n')
        output_file.write(f'Description: {description}\n\n')

# Print confirmation that parsing is complete
print("Parsed alerts have been saved to 'parsed_alerts.txt'.")
