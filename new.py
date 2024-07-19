# Function to encrypt a message using a substitution cipher
def encrypt_message(message, key):
    encrypted_message = []
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) + key  # Shift the character by the key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message.append(chr(shifted))  # Convert back to character and append
        else:
            encrypted_message.append(char)  # Append non-alphabetic characters unchanged
    return ''.join(encrypted_message)

# Function to decrypt a message using a substitution cipher
def decrypt_message(encrypted_message, key):
    decrypted_message = []
    for char in encrypted_message:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_message.append(chr(shifted))
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)

# Example usage
if __name__ == "__main__":
    # Encrypt a message
    message = "Hello, this is a secret message!"
    key = 3
    encrypted_message = encrypt_message(message, key)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Decrypted Message: {decrypted_message}")
