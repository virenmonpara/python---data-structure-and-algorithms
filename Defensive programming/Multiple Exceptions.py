age = -1
while age <= 0:
    try:
        age = int(input("enter your age in years: "))
        if age <= 0:
            print("age must be positive")
    except ValueError:
        print("there is an invalid age specification")
    except EOFError:
        print("there was an error reading input")

# another example for the same method
"""

age=-1
while age<=0:
    try:
        age=int(input("enter your age in years: "))
        if age<=0:
            print("age must be positive")
    except ValueError as e:         # will give description of error
        print(f"unable to process input: {e}")
    except EOFError:
        print("there was an error reading input")

"""

# another example for the same method
""" age=-1
while age<=0:
    try:
        age=int(input("enter your age in years: "))
        if age<=0:
            print("age must be positive")
    except (ValueError,EOFError) as e:          # both error in one sentence
        print(f"unable to process input : {e}") """
