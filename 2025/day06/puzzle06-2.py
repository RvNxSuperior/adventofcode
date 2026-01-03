import os

path = '2025\day06\input.txt'

with open(path) as file:

    input = file.read()


inputList = input.splitlines()


lines = []

for line in range(len(inputList) - 1):

    lines.append([])




# split lines into usable substrings

operator = inputList[-1].split()

count = 0

line1Temp = ''
line2Temp = ''
line3Temp = ''
line4Temp = ''

for column in range(len(inputList[0])):

    if inputList[0][column] == inputList[1][column] == inputList[2][column] == inputList[3][column] == ' ':

        lines[0].append(line1Temp)
        lines[1].append(line2Temp)
        lines[2].append(line3Temp)
        lines[3].append(line4Temp)

        line1Temp = ''
        line2Temp = ''
        line3Temp = ''
        line4Temp = ''

    else:

        line1Temp += inputList[0][column]
        line2Temp += inputList[1][column]
        line3Temp += inputList[2][column]
        line4Temp += inputList[3][column]
        
#        if inputList[0][column] != ' ':
#            line1Temp += inputList[0][column]
#        else:
#            line1Temp += '0'
#        
#        if inputList[1][column] != ' ':
#            line2Temp += inputList[1][column]
#        else:
#            line2Temp += '0'
#        
#        if inputList[2][column] != ' ':
#            line3Temp += inputList[2][column]
#        else:
#            line3Temp += '0'
#        
#        if inputList[3][column] != ' ':
#            line4Temp += inputList[3][column]
#        else:
#            line4Temp += '0'



    if column == len(inputList[0]) - 1:

        lines[0].append(line1Temp)
        lines[1].append(line2Temp)
        lines[2].append(line3Temp)
        lines[3].append(line4Temp)

        line1Temp = ''
        line2Temp = ''
        line3Temp = ''
        line4Temp = ''


print(f'Line 1: {len(lines[0])}')
print(f'Line 2: {len(lines[1])}')
print(f'Line 3: {len(lines[2])}')
print(f'Line 4: {len(lines[3])}')

if len(lines[0]) == len(lines[1]) == len(lines[2]) == len(lines[3]):
    print('Success!')

#print(line1)
#print()
#print()
#print(line2)
#print()
#print()
#print(line3)
#print()
#print()
#print(line4)


# computing formulas

sum = 0

for count in range(len(lines[1])):

    print(f'{count:<4}: ', end='')

    if operator[count] == '+':

        sumTemp = 0

        for number in range(len(lines[1][count])):

            activeCount = 0

            temp = 0

            for line in range(len(lines)):

                if lines[3 - line][count][number] != ' ':

                    temp += int(lines[3 - line][count][number]) * (10 ** (activeCount))

                    activeCount += 1

                elif lines[3 - line][count][number] == ' ' and temp != 0:

                    #temp = int(temp / 10)
                    pass

            sumTemp += temp

            print(f' {temp:<4} ', end='|')



    else:

        sumTemp = 1

        for number in range(len(lines[1][count])):

            activeCount = 0

            temp = 0

            for line in range(len(lines)):

                if lines[3 - line][count][number] != ' ':

                    temp += int(lines[3 - line][count][number]) * (10 ** (activeCount))

                    activeCount += 1

                elif lines[3 - line][count][number] == ' ' and temp != 0:

                    #temp = int(temp / 10)
                    pass

                

            sumTemp *= temp

            print(f' {temp:<4} ', end='|')


    sum += sumTemp

    print(f' {operator[count]:<4} ', end='|')
    print(f' {sumTemp} ')



print()
print(f'Sum: {sum}')