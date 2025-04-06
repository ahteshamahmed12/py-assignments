import random

print("Welcome to guess the number game")
print("Choose the number from (1 to 10)")

secret_number = random.randint(1,10)
attempts = 0

while True:
    guess = (input("Enter your guess number :"))
    
    if not guess.isdigit():
        print("Please enter a valid number")
        continue
    guess = int(guess)
    attempts += 1
    
    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
        
    
    