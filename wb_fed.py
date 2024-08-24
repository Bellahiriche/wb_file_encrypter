from cryptography.fernet import Fernet
import os
import argparse
import sys

def generate_key():
    return Fernet.generate_key()

def save_key(key, key_file):
    try:
        with open(key_file, 'wb') as file:
            file.write(key)
        print(f"Clé sauvegardée dans le fichier {key_file}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde de la clé : {e}")
        sys.exit(1)

def load_key(key_file):
    if not os.path.exists(key_file):
        print(f"Erreur : le fichier {key_file} n'existe pas.")
        sys.exit(1)
    
    try:
        with open(key_file, 'rb') as file:
            return file.read()
    except Exception as e:
        print(f"Erreur lors du chargement de la clé : {e}")
        sys.exit(1)

def encrypt_file(input_file, output_file, key):
    if not os.path.exists(input_file):
        print(f"Erreur : le fichier {input_file} n'existe pas.")
        sys.exit(1)

    try:
        with open(input_file, 'rb') as file:
            data = file.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        with open(output_file, 'wb') as file:
            file.write(encrypted_data)

        print(f"Fichier {input_file} encrypté avec succès dans {output_file}")
    except Exception as e:
        print(f"Erreur lors de l'encryption du fichier : {e}")
        sys.exit(1)

def decrypt_file(input_file, output_file, key):
    if not os.path.exists(input_file):
        print(f"Erreur : le fichier {input_file} n'existe pas.")
        sys.exit(1)

    try:
        with open(input_file, 'rb') as file:
            encrypted_data = file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(output_file, 'wb') as file:
            file.write(decrypted_data)

        print(f"Fichier {input_file} décrypté avec succès dans {output_file}")
    except Exception as e:
        print(f"Erreur lors du décryptage du fichier : {e}")
        sys.exit(1)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Encryption et décryption de fichiers avec Fernet.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Commandes disponibles")

    # Commande pour générer une clé
    parser_genkey = subparsers.add_parser('generate_key', help="Génère une clé symétrique")
    parser_genkey.add_argument('key_file', help="Fichier où la clé sera sauvegardée")

    # Commande pour encrypter un fichier
    parser_encrypt = subparsers.add_parser('encrypt', help="Encrypte un fichier")
    parser_encrypt.add_argument('input_file', help="Fichier à encrypter")
    parser_encrypt.add_argument('output_file', help="Fichier où sauvegarder le fichier encrypté")
    parser_encrypt.add_argument('key_file', help="Fichier contenant la clé d'encryption")

    # Commande pour décrypter un fichier
    parser_decrypt = subparsers.add_parser('decrypt', help="Décrypte un fichier")
    parser_decrypt.add_argument('input_file', help="Fichier à décrypter")
    parser_decrypt.add_argument('output_file', help="Fichier où sauvegarder le fichier décrypté")
    parser_decrypt.add_argument('key_file', help="Fichier contenant la clé de décryptage")

    return parser.parse_args()

def main():
    """Point d'entrée principal du script."""
    args = parse_arguments()

    if args.command == 'generate_key':
        key = generate_key()
        save_key(key, args.key_file)

    elif args.command == 'encrypt':
        key = load_key(args.key_file)
        encrypt_file(args.input_file, args.output_file, key)

    elif args.command == 'decrypt':
        key = load_key(args.key_file)
        decrypt_file(args.input_file, args.output_file, key)

if __name__ == "__main__":
    main()
