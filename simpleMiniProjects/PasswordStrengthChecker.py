import re

# List of common passwords to check against
COMMON_PASSWORDS = ['password', "12345", "qwerty", "111111", "abc123"]

def check_password_strength(password):
    # Initialize score variable
    score = 0

    # 1. Check if password length is at least 8 characters
    if len(password) >= 8:
        score += 1
    else:
        print("Password too short. Minimum length should be 8 characters.")

    # 2. Check for both uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        print("Password should contain both uppercase and lowercase letters.")

    # 3. Check for at least one numeric digit
    if re.search(r'[0-9]', password):
        score += 1
    else:
        print("Password should contain at least one number.")

    # 4. Check for at least one special character
    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        print("Password should contain at least one special character (e.g., @, $, !, %, *, ?, &).")

    # 5. Check if password is in common password list (easy to guess)
    if password.lower() in COMMON_PASSWORDS:
        print("Password is too common and easy to guess!")
        return "Weak"

    # 6. Check for sequential numbers (e.g., "123", "234")
    if re.search(r'(012|123|234|345|456|567|678|789)', password):
        print("Password should not contain sequential numbers.")
        return "Weak"
    
    # Final evaluation based on score
    if score >= 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    else:
        return "Weak. Please change."

# Main program to test password strength
password = input("Enter a password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
