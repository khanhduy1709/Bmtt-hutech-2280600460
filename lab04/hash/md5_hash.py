def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    # Initialize variables
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # Pre-processing: padding the message
    original_length = len(message) * 8
    message += b'\x80'
    while (len(message) * 8 + 64) % 512 != 0:
        message += b'\x00'
    message += original_length.to_bytes(8, byteorder='little')

    # Process the message in 512-bit blocks
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], byteorder='little') for j in range(0, 64, 4)]

        a, b, c, d = a0, b0, c0, d0

        # Main loop
        for i in range(64):
            if i < 16:
                f = (b & c) | ((~b) & d)
                g = i
            elif i < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * i) % 16

            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + f + 0x100000000 + words[g]) & 0xFFFFFFFF, 7)) & 0xFFFFFFFF
            a = temp

        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF

    # Produce the final hash value
    return f"{a0:08x}{b0:08x}{c0:08x}{d0:08x}"

input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))
print(f"Giá trị băm MD5 của chuỗi '{input_string}' là: {md5_hash}")