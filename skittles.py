'''
This program's goal is to allow the user to guess a number between 0 and 1023
inclusive. The program picks the number and if the user picks the correct number,
they will get a message. This code was made by Julian.
'''

'''
This block shows the maximum number of the candy that the machine can hold
and tells the computer to pick a number between 0 and 1023 inclusive.
'''
import random
candyGuess = 1024
numberOfCandy = random.randint(0, 1023)

'''
This block of code shows that while the user's guess is not equal to
to the computers pick, run the program again.
'''
while candyGuess != numberOfCandy:
    while True:
        try:
            candyGuess = int(input("Guess how many candies are in the machine!"))
            if candyGuess < 0:
                '''
                If the user puts an input that is invalid (negative numbers or symbols), the
                code will reprompt the user.
                '''
                print("Please put a positive number.")
                continue
            break
        except ValueError:
            print("That's not a valid input")
    if candyGuess < numberOfCandy:
        print("That guess is too low! Guess again!")
    elif candyGuess > numberOfCandy:
        print("That guess is too high! Guess again!")

'''
When the user's guess is equal to the computer's pick, the program will
print this:
'''
print("That's it! You got it!")
