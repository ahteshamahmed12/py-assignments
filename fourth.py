import random

print("Welcome to guess the number game where computer guess the number")
print("Choose the number from (1 to 10)")

user=int(input("Enter your number :"))

low=1
high=10
feedback=[]

while True:
    if feedback != "c":
        computer=random.randint(low,high) 
        print(f"Computer guess the number {computer}")
        feedback= input("If guess too high (h) if guess too low (l) and guess is correct  (c)").lower()
        
        if feedback == "h":
            high=computer-1
        elif feedback == "l":
            low=computer+1
        elif feedback == "c":
            print(f"Computer guessed your number {computer} correctly")
            break
