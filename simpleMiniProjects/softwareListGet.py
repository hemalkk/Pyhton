import subprocess

# Create a batch file to query installed software from the Windows registry
batch_content = """
@echo off
reg query HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall /s > software.txt
"""
with open("get_software_list.bat", "w") as batch_file:
    batch_file.write(batch_content)

#Execute the batch file to generate the software.txt file
subprocess.run(["get_software_list.bat"], shell=True)

#Read software.txt and extract software names
software_names = []
with open("software.txt", "r") as file:
    for line in file:
        # Look for lines containing 'DisplayName' to find software names
        if "DisplayName" in line:
            # Extract the software name and strip any extra spaces
            software_name = line.split("    ")[-1].strip()
            software_names.append(software_name)

#Write the extracted software names to final_soft.txt
with open("final_soft.txt", "w") as final_file:
    for name in software_names:
        final_file.write(name + "\n")

print("Software names have been written to final_soft.txt")
