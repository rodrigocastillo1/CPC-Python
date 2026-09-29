def getDigitListInString(str):
    digits = [int(c) for c in str if c.isdecimal()]
    return digits

def main():
    print("This program will return the sum and average of the digits that appear in the input string.")
    raw_in = input("Please enter your string, e.g. \"I was born in 1991.\"\n>> ")
    digitList = getDigitListInString(raw_in)
    if not digitList:
        print("There are no digits in the input string.")
        return
    
    print("The sum of the digits in the string is: ", sum(digitList))
    print("The avg of the digits in the string is: ", sum(digitList)/len(digitList))

if __name__ == "__main__":
    main()