def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# --- User input ---
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))

# --- Encryption ---
encrypted_msg = encrypt(message, shift)
print("Encrypted:", encrypted_msg)

# --- Decryption ---
decrypted_msg = decrypt(encrypted_msg, shift)
print("Decrypted:", decrypted_msg)
