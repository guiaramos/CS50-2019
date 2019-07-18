# Modules
import sys
from cs50 import get_string

# Check for the key provided
if len(sys.argv) != 2:
    print("Usage: ./caesar k")
    sys.exit(1)

# Assigning the key
key = int(sys.argv[1])

# Getting the plaintext
plaintext = get_string("plaintext: ")

# Start the script
print("ciphertext: ", end="")

for char in plaintext:
    if not char.isalpha():
        print(char, end="")
        continue

    # offset in case of uppercase or lowercase
    ascii_offset = 65 if char.isupper() else 97

    c = ord(ch) - ascii_offset
    cipher = (c + key) % 26

    print(chr(cipher + ascii_offset), end="")

print()