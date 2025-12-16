message = input("Enter message: ")
encoded = ""

for char in message:
    encoded += chr(ord(char) + 1)

print("Encoded message:", encoded)