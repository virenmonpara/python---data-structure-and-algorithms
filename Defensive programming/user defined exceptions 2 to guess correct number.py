#  Python user-defined exceptions to guess correct number
class Error(Exception):
    #Base class for other exceptions (abstract class)
    pass


class ValueTooSmallError(Error):
    #Raised when the input value is too small
    pass


class ValueTooLargeError(Error):
    #Raised when the input value is too large
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter integer number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!",'\n')
    except ValueTooLargeError:
        print("This value is too large, try again!",'\n')

print("Congratulations! You guessed it correctly.")