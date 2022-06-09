import random

from numpy import number

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*-+/\?"

use_for_password = lower_case + upper_case + number + symbols
length_for_password = int(input("How long do you want your password to be? "))
password = print('your generated password is:', "".join(
    random.sample(use_for_password, length_for_password)))
