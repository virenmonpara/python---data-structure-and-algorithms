# user defined exceptions to find if entered age is negative

class NegativeAgeError(Exception):
    pass

try:
    age = int(input("please enter your age :"))
    print(f"Age is: {age}")
    if age <= 0:
        raise NegativeAgeError("please enter correct age")
    yearofBirth = 2021-age
    print(f"Year of Birth is : {yearofBirth}")
except NegativeAgeError:
    print("please enter correct age.")