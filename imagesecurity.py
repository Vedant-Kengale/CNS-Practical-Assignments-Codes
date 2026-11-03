from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

print("Secret Key: ", key.decode())

with open("image.jpg", "rb") as file:
    image = file.read()
    
encrypted = cipher.encrypt(image)

with open("encrypted_image.txt", "wb") as file:
    file.write(encrypted)
    
print("Image encrypted Successfully")

with open("encrypted_image.txt", "rb") as file:
    encrypted_data = file.read()
    
try:
    decrypted = cipher.decrypt(encrypted_data)
    
    with open("decrypted_image.txt", "wb") as file:
        file.write(decrypted)
        
    print("File Decrypted Successfully")
    
except Exception:
    print("Decryption Failed! Image was modified or key is incorrect")
  
