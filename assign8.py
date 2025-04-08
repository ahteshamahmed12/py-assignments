print("Convert feet to inches ")

def converter():
    feet=int(input("Enter feet to convert to inches:  "))
    inches=feet*12
    print(f"{feet} feet is {inches} inches")
    
if __name__ == '__main__':
    converter()