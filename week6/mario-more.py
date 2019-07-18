# Modules
from cs50 import get_int

# Condition for getting the input from the user
while True:
    answer = get_int("please, input the height desired between 1 and 8: ")
    if 1 <= answer <= 8:
        break 

# Printing the value inputted by the user
print(f"Height: {answer}")

# Adding one to the answer in reason to printout the correct #s
answer += 1

# Loop for print the pyramid
for n in range(1, answer):
   
    print(" " * (answer - n), end="")    
    print("#" * n, end="")
    print(" ", end="")
    print("#" * n, end="")
    print()
