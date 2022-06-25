numbers = [1.5, 2.3, 0.7, -5, 4.4]
total = 0.0
for num in numbers:
    assert num > 0.0, "numbers must be positive"
    total += num
print('total is:', total) #here assertion throw an error because of negative number

"""The purpose of assertions is:
• Help to ensure that no new bugs are introduced while adding
features or fixing other bugs.
• Document and test the code to a certain extent"""