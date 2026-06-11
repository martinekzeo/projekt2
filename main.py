"""
main.py: druhý zábavný projekt 

author: Martin Páník
email: martinek@cosmicboosts.store
"""
import random

line = "-" * 40
cislo = ""

while len(cislo) < 4:
    digit = str(random.randint(0, 9))

    if len(cislo) == 0 and digit == "0":
        continue

    if digit in cislo:
        continue

    cislo = cislo + digit

print("Hi there!")
print(line)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(line)

attempts = 0

while True:
    guess = input("Enter a number: ")

    if len(guess) != 4:
        print("The number must have 4 digits.")
        print(line)
    elif not guess.isdigit():
        print("You must enter only digits.")
        print(line)
    elif guess[0] == "0":
        print("The number cannot start with 0.")
        print(line)
    elif len(set(guess)) != 4:
        print("Please enter 4 unique numbers.")
        print(line)
    else:
        attempts = attempts + 1
        bulls = 0
        cows = 0

        for i in range(4):
            if guess[i] == cislo[i]:
                bulls = bulls + 1
            elif guess[i] in cislo:
                cows = cows + 1

        print(line)
        print(f"{bulls} bulls, {cows} cows")
        print(line)

        if bulls == 4:
            print("Correct, you've guessed the right number")
            print(f"in {attempts} guesses!")
            print("That's amazing!")
            exit()
