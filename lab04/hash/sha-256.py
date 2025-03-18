import hashlib

def calculate_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

input_string = input("Nhập chuỗi cần băm: ")
hash_value = calculate_sha256(input_string)
print(f"Giá trị băm SHA-256 của chuỗi '{input_string}' là: {hash_value}")