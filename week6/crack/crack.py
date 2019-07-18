# Modules
import sys
import crypt

#  Validation for input
if len(sys.argv) != 2:
    print("Usage: crack <hash>")
    sys.exit(1)

# Variables
hash_ = sys.argv[1]
salt = hash_[0:2]
letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Start script
for fifth in letters:
    for fourth in letters:
        for third in letters:
            for second in letters:
                for first in letters[1:]:
                    candidate = f"{first}{second}{third}{fourth}{fifth}".strip()

                    if crypt.crypt(candidate, salt) == hash_:
                        print(candidate)
                        sys.exit(0)
