import os
import re

path = '2025\day02\input.txt'

with open(path) as file:
    input = file.read()

inputList = re.split(r',|\s', input)
inputList.pop()

IdList = []

for IdRange in inputList:
    rangeList = IdRange.split('-')
    rangeLow = int(rangeList[0])
    rangeHigh = int(rangeList[1])

    print()
    print(rangeList)
    print()

    for num in range(rangeLow, rangeHigh+1):
        numStr = str(num)
        numLen = len(numStr)

        if numLen % 2 == 0:
            
            if numStr[0:int(numLen/2)] == numStr[int(numLen/2):]:
                IdList.append(num)
                print(num)


print(IdList)

sum = 0

for entry in IdList:
    sum += entry


print()
print(f'Sum: {sum}')