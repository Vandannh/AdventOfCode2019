import math
total = 0
temp = 0
with open("input.txt") as file:
    for line in file:
        temp = math.floor(int(line) / 3) - 2
        total += temp

print(total)
