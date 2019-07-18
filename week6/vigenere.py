# Modules
import sys
from cs50 import get_string

# Check if key was informed and assign it
try:
    key = sys.argv[1]
    lenKey = len(key)
    j = 0
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
    
        # check if key is finished
        if j == lenKey:
            j = 0
        
        # assigning the  key
        if key[j].islower():
            k = (ord(key[j]) - 97)
        else:
            k = (ord(key[j]) - 65)

        # incrementing j
        j += 1
        
        if i.islower():
            c = ((((ord(i) + k) - 97) % 26 ) + 97)
        else:
            c = ((((ord(i) + k) - 65) % 26 ) + 65)

        print(chr(c), end="")

    else:
        print(i, end="")

    