if __name__ == '__main__':
    print("This program converts different data types and outputs the results.")

    print("1. Convert an integer to a floating-point number.")
    zahlen = 10
    kommazahlen = float(zahlen)
    print("   zahlen: ", zahlen, type(zahlen), " -> kommazahlen: ", kommazahlen, type(kommazahlen))

    print("2. Convert a floating-point number to an integer.")
    zahlen = int(kommazahlen)
    print("   kommazahlen: ", kommazahlen, type(kommazahlen), " -> zahlen: ", zahlen, type(zahlen))

    print("3. Convert an integer to a string.")
    text = str(zahlen)
    print("   zahlen: ", zahlen, type(zahlen), " -> text: " + text, type(text))

    print("4. Convert a string containing a number to an integer.")
    zahlen = int(text)
    print("   text: " + text, type(text), " -> zahlen: ", zahlen, type(zahlen))

    print("5. Convert an integer to a Boolean")
    wahrheitswert = bool(zahlen)
    print("   zahlen: ", zahlen, type(zahlen), " -> wahrheitswert: ", wahrheitswert, type(wahrheitswert))
