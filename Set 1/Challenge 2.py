### Fixed XOR
# Input: 1c0111001f010100061a024b53535009181c
# Output: 746865206b696420646f6e277420706c6179

import binascii

def XOR(buffer1, buffer2):
    # Convert both buffers to bytes
    buffer1_bytes = bytes.fromhex(buffer1)
    buffer2_bytes = bytes.fromhex(buffer2)

    # Check if buffers are of equal length
    if len(buffer1_bytes) != len(buffer2_bytes):
        print("Buffers are not equal in length")
        return

    output = bytearray(len(buffer1_bytes))
    # Bitwise XOR of each character in buffers
    for i in range(len(buffer1_bytes)):
        output[i] = buffer1_bytes[i] ^ buffer2_bytes[i]
    return binascii.hexlify(bytes(output)).decode("ascii")

# Testing
output = XOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
assert(output == "746865206b696420646f6e277420706c6179")