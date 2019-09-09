import random
candyGuess = 1024
numberOfCandy = random.randint(0, 1023)

while candyGuess != numberOfCandy:
    while True:
        try:
            candyGuess = int(input("Guess how many candies are in the machine!"))
            if candyGuess < 0:
                print("Please put a positive number.")
                continue
            break
        except ValueError:
            print("That's not a valid input")
    if candyGuess < numberOfCandy:
        print("That guess is too low! Guess again!")
    elif candyGuess > numberOfCandy:
        print("That guess is too high! Guess again!")
print("That's it! You got it!")
