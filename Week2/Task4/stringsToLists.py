def stringToList(str):
    return [c for c in str]

def main():
    print("This program will convert a list of strings into a list of lists.")
    list_str = ["Hello, World!", "Lorem ipsum", "dolor sit amet", "consectetur", "adipiscing", "elit"]
    print("Initial list of strings: ", list_str)
    print("-------------------------")
    print("List of lists:")
    res = map(lambda s: list(s), list_str)
    for l in res:
        print(l)

if __name__ == "__main__":
    main()