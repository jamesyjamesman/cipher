# Obtains the word to shift from the user
original_message = message = input("Enter a word to shift.\n")

# Set up empty list
new_word = list()

# Initialize variables
valid = False
amount = 0

# Does the inside code for however many letters are in the message
for letter in message:
    while True:
        # This loop always runs once, but if the number is too large
        # And fails in the encryption step, it runs again to try and get a valid number
        while not valid:
            # If the input is valid, save the amount to shift by, then continue with the rest of the code
            try:
                amount = int(input("How much would you like to shift the word by?\n"))
                break

            # Otherwise, tell the user it is invalid, then repeat the process
            except ValueError:
                print("Enter a number!")

        # If the amount is valid, fill a list with the encrypted letters
        try:
            message = chr(ord(letter) + amount)
            new_word.append(message)
            # Stops the code from asking for an input every time a letter is encrypted
            valid = True
            break
        # Otherwise, print an error, and reset
        except ValueError:
            print("You cannot shift by that much!")
        except OverflowError:
            print("You cannot shift by that much!")

# Combines the new_word list into a string
new_word = "".join(new_word)

# Prints the original message and the new word for comparison
print(f"Your message: {original_message}")
print(f"Shifted word: {new_word}")