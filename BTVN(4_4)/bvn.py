def encode(text, mapping):
    result = ""
    for char in text:
        if char in mapping:
            result += mapping[char]
        else:
            result += char
    return result

def decode(text, mapping):
    reverse_mapping = {v: k for k, v in mapping.items()}
    result = ""
    for char in text:
        if char in reverse_mapping:
            result += reverse_mapping[char]
        else:
            result += char
    return result

mapping = {'a': '!', 'b': '@', 'c': '#', 'd': '$'}

text = "abcd hello"

encoded = encode(text, mapping)
print("Mã hóa:", encoded)

decoded = decode(encoded, mapping)
print("Giải mã:", decoded)