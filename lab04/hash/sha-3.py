from Crypto.Hash import SHA3_256

def calculate_sha3(input_string):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(input_string.encode('utf-8'))
    return sha3_hash.hexdigest()

input_string = input("Nhập chuỗi cần băm: ")
hash_value = calculate_sha3(input_string)
print(f"Giá trị băm SHA-3 của chuỗi '{input_string}' là: {hash_value}")