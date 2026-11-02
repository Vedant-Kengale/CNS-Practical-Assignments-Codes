def encrypt(plaintext, key):
    encrypted = ""

    for i in range(len(plaintext)):

        p = ord(plaintext[i])
        k = ord(key[i % len(key)])
        encrypted_value = p ^ k

        encrypted += format(encrypted_value,'02x')
    return encrypted

def decrypt(ciphertext, key):
    decrypted = ""
    encrypted_bytes = bytes.fromhex(ciphertext)

    for i in range(len(encrypted_bytes)):

        c = encrypted_bytes[i]
        k = ord(key[i % len(key)])
        original_value = c ^ k

        decrypted += chr(original_value)
    return decrypted

# Main Program
print("Custom Encryption and Decryption")

plaintext = input("Enter Message: ")
key = input("Enter Secret Key: ")

if key == "":
    print("Error: Key cannot be Empty")
else:
    # Encryption
    ciphertext = encrypt(plaintext, key)
    print("Encrypted Message: ", ciphertext)

    # Decryption
    original_message = decrypt(ciphertext, key)
    print("Decrypted Message: ", original_message)

    if original_message == plaintext:
        print("Encryption and Decryption Successfull")
