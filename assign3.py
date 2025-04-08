def main():
    degree_fahrenheight=int(input("Enter a temperature in Fahrenheit: ")) 
    degree_celsius=(degree_fahrenheight -32)*5/9
    print(f"The temperature in Celsius is {degree_celsius:.4f} degrees.")



if __name__ == '__main__':
    main()