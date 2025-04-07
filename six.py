import random

print("Welcome to the Hangman game ")
print("let start the game")

options=["cow","goat","sheep","hen","duck","horse","donkey","camel","buffalo","elephant"]
computer=random.choice(options)
guess = 0

while True:
    user=input("Enter your guess:").lower()
    if user == computer:
        print(f"Your guess is correct")
        break
    else:
        guess += 1
        print(f"Your guess is wrong, try again")
        if guess == 5:
            print("You lose")
            break







        
        