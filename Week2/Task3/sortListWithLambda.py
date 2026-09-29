def sortListBy(ld, sortKey):
    sld = sorted(ld, key=lambda d: str(d[sortKey]))
    return sld

def main():
    print("This program will sort a list of dictionaries by the model key.")
    ld = [{'make': 'Google', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
    print("Original list of dicts: ", ld)
    print("-----------------------------")
    print("Sorted by model: ", sortListBy(ld, 'model'))
    print("-----------------------------")
    print("Sorted by make: ", sortListBy(ld, 'make'))
    print("-----------------------------")
    print("Sorted by color: ", sortListBy(ld, 'color'))

if __name__ == "__main__":
    main()