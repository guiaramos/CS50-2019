# Modules
import sys
from cs50 import get_string

# Check if key was informed and assign it
try:
    key = int(sys.argv[1])
except IndexError:
    print("Usage: ./caesar key")
    sys.exit()

# Print key
print (f"the key provided is: {key}")

# Ask for the plaintext to be ciphered
plaintext = get_string("plaintext: ")

# Start cipher
print("ciphertext: ", end="")

for i in plaintext:
   
    if i.isalpha():
        if i.islower():
            c = ((((ord(i) + key) - 97) % 26 ) + 97)
        else:
            c = ((((ord(i) + key) - 65) % 26 ) + 65)
        print(chr(c), end="")
    else:
        print(i, end="")