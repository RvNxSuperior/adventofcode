import os

path = '2025\day06\input.txt'

with open(path) as file:

    input = file.read()


# processing input
inputList = input.splitlines()

line1 = inputList[0].split()
line2 = inputList[1].split()
line3 = inputList[2].split()
line4 = inputList[3].split()
operator = inputList[4].split()

sum = 0

for count in range(len(line1)):

    print(f'Count: {count}')

    if operator[count] == '+':

        result = int(line1[count]) + int(line2[count]) + int(line3[count]) + int(line4[count])

        print(result)

        sum += result

    else:

        result = int(line1[count]) * int(line2[count]) * int(line3[count]) * int(line4[count])

        print(result)

        sum += result

    print()


print(f'Sum: {sum}')