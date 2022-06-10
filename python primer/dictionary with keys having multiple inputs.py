
# Python code to demonstrate a dictionary
# with multiple inputs in a key.
import random as rn

# creating an empty dictionary
dict = {}

# Insert first triplet in dictionary
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z

# Insert second triplet in dictionary
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z

# print the dictionary
print(dict)


# another example

# dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"): "Mumbai",
          ("28.33'34.1", "77.06'16.6"): "Delhi"}

print(places)
print('\n')

# Traversing dictionary with multi-keys and creating
# different lists from it
lat = []
long = []
plc = []

for i in places.keys():
    lat.append(i[0])
    long.append(i[1])
    plc.append(places[i])

print("Latitude:", lat)
print("Longitude:", long)
print("Places:", plc)
