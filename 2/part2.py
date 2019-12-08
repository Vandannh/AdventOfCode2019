
with open("input.txt") as f:
    text = f.read()
    data = list(map(int, text.split(",")))

for noun in range(0,100):
    for verb in range(0,100):
        ls = data.copy()
        ls[1] = noun
        ls[2] = verb
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
        if(ls[0] == 19690720):
            print(100 * noun + verb)

