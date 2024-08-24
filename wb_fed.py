from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key,key_file):
    with open(key_file,'wb') as file:
        file.write(key)

def load_key(key_file):
    with open (key_file,'wb') as file:
        return file.read()

def encrypt_file(input_file,output_file,key):
    with open(input_file,'rb') as file:
        data=file.read()
    
    fernet=Fernet(key)
    encrypt_data=fernet.encrypt(data)

    with open(output_file,'wb') as file:
        file.write(encrypt_data)

def decrypt_file(input_file,output_file,key):
    with open(input_file,'rb') as file:
        encrypted_data=file.read()
    
    fernet=Fernet(key)
    decrypted_data=fernet.decrypt(encrypted_data)

    with open(output_file,'wb') as file:
        file.write(decrypted_data)