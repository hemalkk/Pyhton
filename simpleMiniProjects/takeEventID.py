import subprocess  # To run PowerShell commands
import datetime    # To handle date and time

def fetch_event_logs(log_name, event_id):
    # Calculate the date 5 days ago
    five_days_ago = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%dT%H:%M:%S")

    # Construct the PowerShell command
    powershell_command = f"Get-WinEvent -FilterHashtable @{{LogName='{log_name}'; Id={event_id}; StartTime='{five_days_ago}'}}"

    # Execute the PowerShell command and capture the output
    result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True, shell=True)

    # Save the output to a text file if events were found
    if result.stdout:
        with open("event_logs.txt", "w") as file:
            file.write(result.stdout)
        print("Success.")
    else:
        print("Not success.")


# Get the log name and event ID from the user
log_name = input("Enter the log name (e.g., Security, Application, System): ")
event_id = input("Enter the event ID: ")
fetch_event_logs(log_name, event_id)
