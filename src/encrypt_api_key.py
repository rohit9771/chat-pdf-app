# encrypt_api_key.py

from cryptography.fernet import Fernet

def generate_and_save_key():
    # Generate a key
    key = Fernet.generate_key()
    # Save the key to a file
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def encrypt_api_key(api_key):
    # Load the key
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

    # Initialize the Fernet instance
    cipher_suite = Fernet(key)

    # Encrypt the API key
    encrypted_api_key = cipher_suite.encrypt(api_key.encode())

    # Save the encrypted API key to a file
    with open("encrypted_api_key.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted_api_key)

if __name__ == "__main__":
    api_key = 'enter openai key'
    generate_and_save_key()
    encrypt_api_key(api_key)
    print("API key encrypted and saved successfully.")
