import os

path = '2025\day01\input.txt'

with open(path) as file:
    input = file.read()

inputList = input.splitlines()

dial = 50
count = 0

for line in inputList:
    print(f'{line}', end=' - ')
    diff = int(line[1:])
    diffTemp = diff
    overturnCount = 0

    if line[0] == 'R':
        dialTemp = (dial + diff) % 100
        
        while dial + diffTemp > 100:
            count += 1
            diffTemp -= 100
            overturnCount += 1


    elif line[0] == 'L':
        dialTemp = (dial - diff) % 100

        while dial - diffTemp < 0:
            count += 1
            diffTemp -= 100
            overturnCount += 1

        if dial == 0 and overturnCount >= 0:
            count -= 1


    else:
        print('Error. Corrupted input!')

    print(dial, end='')

    if dialTemp == 0:
        count += 1 

    print(f' - {count}')

    dial = dialTemp


    


print()
print(f'Count: {count}')