import random

print("Welcome to rock,paper and scissor game ")

options=["rock","paper","scissor"]
user=input("Enter your choice (rock,paper,scissor):").lower()
computer=random.choice(options)
if user == computer:
    print(f"Computer choice is {computer}")
    print("It's a tie")
elif (user == "rock" and computer == "scissor") or  (user == "scissor" and computer == "paper") or (user == "paper" and computer == "rock"):
    print(f"Computer choice is {computer}")
    print("You win")
else:
    print(f"Computer choice is {computer}")
    print("You lose")