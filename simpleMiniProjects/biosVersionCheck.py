import subprocess

def get_BIOS_version():
    try:
        # Execute the wmic command to get BIOS version
        result = subprocess.run(['wmic', 'bios', 'get', 'version'], capture_output=True, text=True, shell=True)

        # Check if the command executed successfully
        if result.returncode == 0:
            # Extract the BIOS version from the output
            BIOS_version = result.stdout.strip().split('\n')[-1].strip()
            return BIOS_version
        else:
            # Print error message if command execution fails
            print("Error: Failed to retrieve BIOS version.")
            return None
    except Exception as e:
        # Print error message if any exception occurs
        print(f"Error: {e}")
        return None
    
def save_to_file(BIOS_version):
    try:
        # Save the BIOS version to a text file
        with open('BIOS_version.txt', 'w') as file:
            file.write(BIOS_version)

        print("BIOS version saved to BIOS_version.txt")
    except Exception as e:
        # Print error message if file saving fails
        print(f"Error: {e}")

def main():
    # Get the BIOS version
    BIOS_version = get_BIOS_version()

    if BIOS_version:
        # Save BIOS version to a file if retrieved successfully
        save_to_file(BIOS_version)
    else:
        print("Failed to retrieve BIOS version.")

if __name__ == "__main__":
    main()
