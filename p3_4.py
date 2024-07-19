from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


key = os.urandom(32)

iv = os.urandom(16)


message = b"Hello, this is a secret message."


padder = padding.PKCS7(128).padder()
padded_data = padder.update(message) + padder.finalize()


cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

print("Encrypted:", ciphertext.hex())

# Decrypt the ciphertext
decryptor = cipher.decryptor()
decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()


unpadder = padding.PKCS7(128).unpadder()
decrypted_message = unpadder.update(decrypted_padded_data) + unpadder.finalize()

print("Decrypted:", decrypted_message.decode())


