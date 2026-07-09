#  h -> m
#  i -> n
#  j -> o
# ...

# cipher = {"a": "f", "b": "g",     "z": "e"}
#  cipher["h"] == "m"


message = input("Enter your message: ")
message = message.lower()

shift = int(input("Shift: "))

alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = {}

for i in range(26):
    cipher[alphabet[i]] = alphabet[(i + shift) % 26]

encoded = ""
for char in message:
    if char in cipher:
        encoded += cipher[char]
    else:
        encoded += char
print(encoded)


decoder = {}
for key, value in cipher.items():
    decoder[value] = key

decoded = ""
for char in encoded:
    if char in decoder:
        decoded += decoder[char]
    else:
        decoded += char
print(decoded)

