name = input("Enter your name (key): ").lower()

# Remove duplicate letters while keeping order
cipher = ""
for ch in name:
    if ch not in cipher and ch.isalpha():
        cipher += ch

# Add remaining letters
for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in cipher:
        cipher += ch

plain = "abcdefghijklmnopqrstuvwxyz"

choice = input("Enter E for Encryption or D for Decryption: ").upper()
text = input("Enter text: ").lower()

result = ""

if choice == "E":   # Encryption
    for ch in text:
        if ch in plain:
            result += cipher[plain.index(ch)]
        else:
            result += ch
    print("Encrypted text:", result)

elif choice == "D":   # Decryption
    for ch in text:
        if ch in cipher:
            result += plain[cipher.index(ch)]
        else:
            result += ch
    print("Decrypted text:", result)

else:
    print("Invalid choice")
