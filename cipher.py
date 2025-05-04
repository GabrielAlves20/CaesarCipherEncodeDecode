alphabet = 'abcdefghijklmnopqrstuvwxyz'

caesar_cipher = {letter: alphabet[(i + 5) % 26] for i, letter in enumerate(alphabet)}

decrypt_cipher = {letter: key for key, letter in caesar_cipher.items()}

def encrypt(text: str) -> str:
    encrypted_text = ""

    for char in text:
        if char.islower():
            encrypted_text += caesar_cipher.get(char, char)
        elif char.isupper():
            encrypted_text += caesar_cipher.get(char.lower(), char).upper()
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text: str) -> str:
    decrypted_text = ""

    for char in encrypted_text:
        if char.islower():
            decrypted_text += decrypt_cipher.get(char, char)
        elif char.isupper():
            decrypted_text += decrypt_cipher.get(char.lower(), char).upper()
        else:
            decrypted_text += char

    return decrypted_text
