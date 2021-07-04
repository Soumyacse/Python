import hashlib
str2hash="harsh"
result=hashlib.md5(str2hash.encode())
print(result.hexdigest())
