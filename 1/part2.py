import math
total = 0
temp = 0
with open("input.txt") as file:
    for line in file:
        fuel = int(line)
        while fuel > 0:
            fuel = math.floor(fuel / 3) - 2
            if(fuel > 0):
                total += fuel
                print(fuel)

print(total)