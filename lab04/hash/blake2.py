import hashlib

def calculate_blake2(input_string):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(input_string.encode('utf-8'))
    return blake2_hash.hexdigest()

input_string = input("Nhập chuỗi cần băm: ")
hash_value = calculate_blake2(input_string)
print(f"Giá trị băm BLAKE2 của chuỗi '{input_string}' là: {hash_value}")