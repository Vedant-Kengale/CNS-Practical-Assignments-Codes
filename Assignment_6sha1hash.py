import hashlib

def generate_sha1(text):
    text_bytes =  text.encode('utf-8')
    sha1_hash = hashlib.sha1(text_bytes)
    return sha1_hash.hexdigest()

message = input("Enter the Original Message: ")

original_hash = generate_sha1(message)

print("\n======Original Message======")
print("Original Message:", message)
print("SHA-1 Hash: ", original_hash)
print("Hash Length: ", len(original_hash), "characters")

modified_message = message + "1"

modified_hash = generate_sha1(modified_message)

print("\n======MODIFIED MESSAGE======")
print("Modified Message: ", modified_message)
print("Modified SHA-1 Hash: ", modified_hash)
print("Hash Length: ", len(modified_hash), "characters")

print("\n======HASH COMPARISON======")

if original_hash == modified_hash:
    print("Both Hashes are Same")
else:
    print("Both Hashes are Different")
    print("Avalanche Effect is Demonstrated")
    
print("\n======FINAL RESULT======")
print("SHA-1 Hashing is performed successfully")
print("SHA-1 Hashing produces a 16-bit hash (40 Hexadecimal characters) digest")
