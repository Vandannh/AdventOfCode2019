
with open("input.txt") as f:
    text = f.read()
    ls = list(map(int, text.split(",")))
i = 0
while ls[i] != 99:
    pos1 = ls[i+1]
    pos2 = ls[i+2]
    pos3 = ls[i+3]
    if(ls[i] == 1):
        ls[pos3] = ls[pos1] + ls[pos2]
    elif(ls[i] == 2):
        ls[pos3] = ls[pos1] * ls[pos2]

        
    i += 4

print(ls[0])