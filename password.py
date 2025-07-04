import re

def check_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])
    
    if score == 5:
        strength = "Very Strong 💪"
    elif score >= 4:
        strength = "Strong ✅"
    elif score >= 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength

# --- Input ---
password = input("Enter your password: ")
result = check_strength(password)
print("Password Strength:", result)
