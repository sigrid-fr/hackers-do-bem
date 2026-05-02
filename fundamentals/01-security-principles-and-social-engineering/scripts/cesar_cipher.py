# -------------------------------------------------------------------------
# Module: 01 - Security Principles & Social Engineering
# Purpose: Demonstrates foundational security concepts and awareness of
#          human-based attack vectors such as social engineering
# -------------------------------------------------------------------------

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


if __name__ == "__main__":
    print("=== Caesar Cipher Tool ===")

    choice = input("Choose: (E)ncrypt or (D)ecrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print(f"Encrypted: {encrypted}")

    elif choice == 'd':
        decrypted = decrypt(message, shift)
        print(f"Decrypted: {decrypted}")

    else:
        print("Invalid option")
