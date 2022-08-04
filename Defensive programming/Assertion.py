numbers = [1.5, 2.3, 0.7, 0.2, 4.4]
total = 0.0
for num in numbers:
    assert num > 0.0, "numbers must be positive"
    total += num
# here assertion throw an error because of negative number
print('total is:', total)

"""The purpose of assertions is:
• Help to ensure that no new bugs are introduced while adding
features or fixing other bugs.
• Document and test the code to a certain extent"""

# another example
# x="hello"
# assert x== "hello" # nothing happens
# assert x== "goodbye" #AssertionError is raised
