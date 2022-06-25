"""try:
    age= int(input("enter your age in years: "))
except ValueError as e:
    print(f"unable to process input")
    raise"""

#
try:
    age= int(input("enter your age in years: "))
except ValueError as e:
    raise RuntimeError("unable to process input") from e

