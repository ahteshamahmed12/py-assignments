import random

print("Welcome to my password generator")

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
number = input("How many passwords do you want to generate? ")
number =int(number)

lenght=input("How long do you want your password to be? ")
lenght=int(lenght)

for password in range(number):
    password=""
    for c in range(lenght):
        password+=random.choice(chars)
    print(password)
print("Password generated successfully")