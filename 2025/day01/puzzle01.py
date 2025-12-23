import os

path = '2025\day01\input.txt'

with open(path) as file:
    input = file.read()

inputList = input.splitlines()

dial = 50
count = 0

for line in inputList:
    print(f'{line}', end=' - ')

    if line[0] == 'R':
        dial = (dial + int(line[1:])) % 100

    elif line[0] == 'L':
        dial = (dial - int(line[1:])) % 100

    else:
        print('Error. Corrupted input!')

    print(dial, end='')

    if dial == 0:

        count += 1
        print(f' - {count}')

    else:
        print()
        pass
    


print()
print(f'Count: {count}')