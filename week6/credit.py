# Modules
from cs50 import get_int
from math import floor

# Variables
digit1 = 0
digit2 = 0
numDigits = 0
sumDoubleOdds = 0
sumEvens = 0

# Asking for input credit card
creditCard = get_int("Number: ")

# Checking the credit card number
while creditCard > 0:
    digit2 = digit1
    digit1 = creditCard % 10

    if numDigits % 2 == 0:
        sumEvens += digit1
    else:
        multiple = 2 * digit1
        sumDoubleOdds += (multiple // 10) + (multiple % 10)

    creditCard //= 10
    numDigits += 1

# Assigning flag
isValid = (sumEvens + sumDoubleOdds) % 10 == 0
first_two_digits = (digit1 * 10) + digit2

if digit1 == 4 and numDigits >= 13 and numDigits <= 16 and is_valid:
    print("VISA\n")
elif first_two_digits >= 51 and first_two_digits <= 55 and numDigits == 16 and is_valid:
    print("MASTERCARD\n")
elif (first_two_digits == 34 or first_two_digits == 37) and numDigits == 15 and is_valid:
    print("AMEX\n")
else:
    print("INVALID\n")
