# bounce.py
#
# Exercise 1.5

initial_height = 100 # (in Meters)
present_height = initial_height
count = 0
distance_reductor = 3/5


while count < 10:
    present_height = present_height * distance_reductor
    print(count, end=" ")
    print(round(present_height, 4))
    count += 1

