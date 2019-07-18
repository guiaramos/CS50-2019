# Modules
import sys
from cs50 import get_string

# Def for gerenating the key
def isValid(key):
    for char in key:
        if not char.isalpha():
            return False
    return True

# Check the input from user
if len(sys.argv) != 2 or not isValid(sys.argv[1]):
    print("Usage: ./vigenere k")
    sys.exit(1)

key = sys.argv[1]
plaintext = get_string("plaintext: ")
j = 0

# Starting script
print("ciphertext: ", end="")

for char in plaintext:
    if not char.isalpha():
        print(char, end="")
        continue

    ascii_offset = 65 if char.isupper() else 97

    pi = ord(char) - ascii_offset
    kj = ord(key[j % len(key)].upper()) - 65
    ci = (pi + kj) % 26
    j += 1

    print(chr(ci + ascii_offset), end="")

print()
