import random
def roll_dice():
   
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    
    print(f"Roll diced 1 : {dice1}")
    print(f"Roll diced 2 : {dice2}")
    total=dice1+dice2
def main():
    print("Rolling two dices three times")
    for dice in range(3):
        print(f"---roll{dice + 1}")
        roll_dice()
        print()
    
if __name__ == '__main__':
    main()
