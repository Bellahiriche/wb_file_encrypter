This script provides a command-line tool for file encryption and decryption using the Fernet encryption algorithm from the cryptography library. It allows users to generate encryption keys, encrypt files, and decrypt files using those keys.

Key Features:
Generate Key: Creates a new symmetric key for encryption.
Encrypt File: Encrypts the contents of a file.
Decrypt File: Decrypts an encrypted file.
How to Use:
Generate a Key:

python script.py generate_key <key_file>
This will generate a key and save it in the specified key_file.


Encrypt a File:

python script.py encrypt <input_file> <output_file> <key_file>
Encrypts the input_file and saves the encrypted data to output_file using the key from key_file.


Decrypt a File:

python script.py decrypt <input_file> <output_file> <key_file>
Decrypts the input_file and saves the decrypted data to output_file using the key from key_file.

