from cryptography.fernet import Fernet

def write_key():  # Generates a key and saves it to a file

    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

'''        
generate_key() function generates a fresh fernet key,
you really need to keep this in a safe place,
if you lose the key, you will no longer be able to decrypt data that was encrypted with this key.
'''

def load_key():  # Loads the key from the current directory named 'key.key
    return open("key.key", "rb").read()

write_key()
key = load_key()
message = "Secret Message Test".encode()
f = Fernet(key)
encrypted = f.encrypt(message)
print(encrypted)

decrypted_encrypted = f.decrypt(encrypted)
print(decrypted_encrypted)