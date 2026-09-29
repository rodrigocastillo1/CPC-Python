import ast

def validateInput(raw_in):
    try:
        u_list = ast.literal_eval(raw_in)
        if type(u_list) != list:
            raise Exception("Not a list.")
        for t in u_list:
            if type(t) != tuple or len(t) != 2:
                raise Exception("Not a valid tuple.")
    except:
        print("Incorrect format. Please enter a valid list of tuples.")
        return (False, [])
    return (True, u_list)

def main():
    print("This program will sort a list of tuples in increasing order by the last element of the tuple.")
    raw_in = input("Please enter the list of tuples in Python format, e.g. [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]\n>> ")
    isInputValid, u_list = validateInput(raw_in)
    if isInputValid:
        s_list = sorted(u_list, key=lambda t : t[1])
        print("The sorted list is: ", s_list)

if __name__ == "__main__":
    main()