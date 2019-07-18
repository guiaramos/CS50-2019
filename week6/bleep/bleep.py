# Modules
from cs50 import get_string
from sys import argv
from pandas import DataFrame

# Start of the class
class main():

    # Checking the info provided by the user
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    # Treating the file and checking if it is valid
    file = []
    try:
        with open(argv[1]) as f:
           for line in f:
               line = line.replace("\n", "")    
               file.append(line)
               file.append(line.upper())
    except:
        print("Usage: python bleep.py dictionary")
        exit(1)

    # Asking for the message:
    print("What message would you like to censor?")
    user_message = get_string("")

    # Transforming the message into list
    message_list = user_message.split(" ")

    # Starting the interations
    for word in range(len(message_list)):
        if message_list[word] in file:
            print("*" * len(message_list[word]), end="")
        else:
            print(message_list[word], end="")
        print(" ", end="")

# Call of the class
if __name__ == "__main__":
    main()