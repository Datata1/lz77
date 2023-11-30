def decode_varint(byte_sequence):
    result = 0
    for byte in byte_sequence:
        result = (result << 7) | (byte & 0x7F)
        if not byte & 0x80:
            break
    return result

def decode_delta(byte_sequence):
    values = [decode_varint(byte_sequence[0:1])]
    for i in range(1, len(byte_sequence)):
        values.append(values[-1] + decode_varint(byte_sequence[i:i+1]))
    return values

# Gegebene Bytes
bytes_sequence = [
    0b10001101, 0b10000101, 0b11110101, 0b10000110,
    0b00000111, 0b10000001, 0b10000010, 0b00000110,
    0b10000001, 0b10101010
]

# Delta-Encoding rückgängig machen
decoded_deltas = decode_delta(bytes_sequence)

# Die ersten beiden Werte repräsentieren Dokument-ID, die nächsten beiden repräsentieren Term-Häufigkeit
index_entries = list(zip(decoded_deltas[0:2], decoded_deltas[2:]))
print("Indexeinträge:", index_entries)
