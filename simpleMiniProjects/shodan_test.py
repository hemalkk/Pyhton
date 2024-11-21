import shodan

# Initialize Shodan API with the provided API key
api_key = "API_KEY"
api = shodan.Shodan(api_key)

try:
    # Search Shodan for Apache servers running on port 80
    query = "apache port:80"
    results = api.search(query)
    
    # Print the total number of results found
    print(f"Results found: {results['total']}")

    # Iterate over each result in the search results
    for result in results['matches']:
        # Extract and display relevant information: IP, port, and data
        ip_address = result['ip_str']
        port = result['port']
        data = result['data']
        
        print(f"IP: {ip_address}")
        print(f"Port: {port}")
        print(f"Data: {data}\n")

except shodan.APIError as e:
    # Handle API errors by printing an error message
    print(f"Error: {e}")
