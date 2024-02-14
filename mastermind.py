# Employing a game called Mastermind that makes you guess from a range of colors
# With a number of tries and lets you know when you get it right

# Importing the function that randoms
import random

# Declaring a variable with a list and number of tries for the game
color_list = ["R", "G", "B", "W", "O", "Y"]
tries = 10
code_length = 4


# Creating a function that picks a random color list using the random function
# And makes a 4 color list
def generate_code():
    code = []
    for _ in range(code_length):
        choice = random.choice(color_list)
        code.append(choice)
    return code


# Creating a function that takes input from the user and
# Checks if it  follows the rules of the game
def guess_color():
    while True:
        guess = input("\nGuess Code: ").upper().split()

        if len(guess) != code_length:
            print("\nIncorrect number of color entries")
            print(f"You must enter only {code_length} colors.")
            continue

        for choice in guess:
            if choice not in color_list:
                print(f"Invalid color: {choice}")
                print(f"TRY AGAIN!!!")
                break
        else:
            break
    return guess


# A function that check if the user input is correct and also
# Checks to see if the input guess is in the correct position
# As well as shows if it is the incorrect position
def check_code(guess, real_code):
    color_count = {}
    correct_position = 0
    incorrect_position = 0

    for choice in real_code:
        if choice not in color_count:
            color_count[choice] = 0
        color_count[choice] += 1

    for guessing_color, real_color in zip(guess, real_code):
        if guessing_color == real_color:
            correct_position += 1
        elif guessing_color in color_count and color_count[guessing_color] > 0:
            incorrect_position += 1
            color_count[guessing_color] -= 1

    return correct_position, incorrect_position


# Main function with the print script and with the number of tries
# As well as mentions when the script is correct
def game():
    print(f"Welcome to Mastermind!!!")
    print(f"You have {tries} tries to guess the code and you valid colors are {color_list}")

    code = generate_code()
    for attempts in range(1, tries + 1):
        guess = guess_color()
        correct_position, incorrect_position = check_code(guess, code)

        if correct_position == code_length:
            print(f"You guessed right with an attempt of {attempts} tries")
            break

        print(f"Correct Position: {correct_position} | Incorrect Position: {incorrect_position}")

    else:
        print("You ran out of tries, the code was: ", *code)


if __name__ == "__main__":
    game()
