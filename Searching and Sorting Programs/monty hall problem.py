import random

greeting = """This is the Monty Hall problem.
There are 3 doors in front of you, and there is a prize behind one of them.
Once you select a door, I will open one of the two you had not selected which does not have a prize behind it.
You will then have the opportunity to switch from the door you originally selected to an alternate door..
if you want to see youtube video : https://youtu.be/4Lb-6rxZxx0 """

print(greeting)

A = "A"
B = "B"
C = "C"

doors = ["A", "B", "C"]

prize = random.choice(doors)
doors.remove(prize)

selection = input("Select door 'A', 'B', or 'C': ")

if selection == prize:
    open_door = random.choice(doors)
    doors.remove(open_door)
    alternate = doors.pop()
else:
    doors.remove(selection)
    open_door = doors.pop()
    alternate = prize

print(f"The door I will now open is: {open_door}")

second_chance = input(
    "Would you like to select the third door? Type 'Yes' or 'No': ")

if second_chance == "Yes":
    if alternate == prize:
        print(
            f"Congrats, you win! The prize was behind the alternate, {alternate}")
    else:
        print(f"Sorry, the prize was behind the original door {prize}")


if second_chance != "Yes":
    if selection != prize:
        print(f"Sorry, the prize was behind the alternate door, {prize}")
    else:
        print(
            f"Congrats, you win! The prize was behind your original selection, {selection}")
