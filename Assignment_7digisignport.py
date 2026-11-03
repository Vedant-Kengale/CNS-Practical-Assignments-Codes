from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

private_key = dsa.generate_private_key(key_size=2048)

public_key = private_key.public_key()
print("Key Created Successfully")

message = input("Enter the Message: ")

message = message.encode('utf-8')

signature = private_key.sign(message, hashes.SHA256())
print("Signature Created Successfully")
print("Signature: ", signature.hex())

# Verify digital signature
try:
    public_key.verify(signature, message, hashes.SHA256())
    
    print("Signature Verified Successfully")
    print("Message is authentic and unchanged")
    
except InvalidSignature:
    print("Signature Verification Failed")
    print("Message may have been modified")
    
modified_message = b"Modified Tendor Document"

# Test Digital signature
try:
    public_key.verify(signature, modified_message, hashes.SHA256())
    
    print("Signature Verified Successfully")
except InvalidSignature:
    print("Signature Verification Failed")
    print("Message has been modified")
