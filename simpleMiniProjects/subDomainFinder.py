import requests
from bs4 import BeautifulSoup

def get_subdomains(url):
   
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.text, 'html.parser')

            # Create a set to store unique subdomains
            subdomains = set()

            # Find all 'a' tags (hyperlinks) in the HTML
            for link in soup.find_all('a'):
                href = link.get('href')

                # Check if the hyperlink starts with 'http://' or 'https://'
                if href and (href.startswith("https://") or href.startswith("http://")):
                    # Extract the subdomain from the hyperlink
                    subdomain = href.split('//')[1].split('/')[0]
                    subdomains.add(subdomain)

            # Save the subdomains to a text file
            with open('subdomains.txt', 'w') as f:
                for subdomain in subdomains:
                    f.write(subdomain + '\n')

            print("Success")

        else:
            print(f"Failed")

    except Exception as e:
        print(f"Error")

# Example usage
url = ""
get_subdomains(url)
