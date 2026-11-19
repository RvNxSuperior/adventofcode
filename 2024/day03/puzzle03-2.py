import re

path = '2024/day03/input.txt'

with open(path) as file:
    data = file.read()


# processing

matches = re.findall(pattern='mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don\'t\\(\\)', string=data)

print(matches)

result = 0

do = True

for entry in matches:

    if entry == 'do()':
        do = True

    elif entry == 'don\'t()':
        do = False

    elif do == True:

        entry = entry.split(',')
        dig1 = int(entry[0][4:])
        dig2 = int(entry[1][:-1])

        result += dig1 * dig2

print(f'Solution: {result}')