import hashlib

string = input()
encoded_data = string.encode()
result = hashlib.sha256(encoded_data).hexdigest()
print(result)
