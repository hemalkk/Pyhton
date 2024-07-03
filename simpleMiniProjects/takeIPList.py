import subprocess

# Function to run a command and capture its output
def run_command(command):
    # Run the command and capture its output
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout  # Return the output as text

# Main function to extract foreign IP addresses from netstat output
def extract_foreign_ips(netstat_output):
    ips = []  # Initialize an empty list to store IP addresses
    lines = netstat_output.splitlines()  # Split the output into lines
    for line in lines:
        columns = line.split()  # Split each line into columns
        if len(columns) >= 3:
            foreign_address = columns[2]  # Get the foreign address from the 3rd column
            ips.append(foreign_address)  # Append the foreign address to the list
    return ips  # Return the list of IP addresses

# Run the netstat command to get active connections
netstat_output = run_command(['netstat', '-ano'])

# Extract foreign IPs from netstat output
foreign_ips_list = extract_foreign_ips(netstat_output)

# Save Foreign IPs to a text file
with open('foreign_ips.txt', 'w') as file:
    for ip in foreign_ips_list:
        file.write(ip + '\n')  # Write each IP address to the file, one per line

print("Success.")  # Print success message
