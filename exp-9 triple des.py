from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

# Take key
key = input("Enter 24-character key: ").encode()

# Create cipher
cipher = DES3.new(key, DES3.MODE_ECB)

choice = input("Enter E to Encrypt or D to Decrypt: ")

if choice.upper() == 'E':
    text = input("Enter plain text: ").encode()
    encrypted = cipher.encrypt(pad(text, 8))
    print("Encrypted Text:", encrypted)

elif choice.upper() == 'D':
    text = eval(input("Enter encrypted text: "))
    decrypted = unpad(cipher.decrypt(text), 8)
    print("Decrypted Text:", decrypted.decode())
