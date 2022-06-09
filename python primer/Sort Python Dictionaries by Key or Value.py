def dictionary():
    mydict = {}

# Initializing value
    mydict[2] = 565
    mydict[1] = 12
    mydict[5] = 12
    mydict[4] = 4
    mydict[6] = 1
    mydict[3] = 33

    print("Task 1:-\n")
    print("Keys are")

    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i in sorted(mydict.keys()):
        print(i, end=" ")


def main():
    # function calling
    dictionary()


if __name__ == "__main__":
    main()
