def main():
    print("This program will calculate the factorial of a given number.")
    n = input("Please enter your number. Only integers will be considered \n>> ")
    if not n.isdigit():
        print("Invalid value. Please enter positive integer numbers only.")
        return
    
    n = int(n)
    r = 1
    for i in range (1, n+1):
        r = r*i

    print(n, "! = ", r)

if __name__ == "__main__":
    main()
