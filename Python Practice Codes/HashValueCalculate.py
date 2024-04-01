import hashlib

# Prompt the user to enter some input
data = input("Please Enter Some Input: ")

# Encode the input string to bytes
encoded_data = data.encode()

# Create a hash object using the SHA-256 algorithm
hash_object = hashlib.sha256()

# Update the hash object with the encoded data
hash_object.update(encoded_data)

# Get the hexadecimal representation of the hash value
hash_value = hash_object.hexdigest()

# Print the original input string and its corresponding hash value
print("Hash Value '{}' of Input is = '{}'".format(data, hash_value))
