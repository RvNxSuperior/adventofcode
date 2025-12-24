import os
import re
import math

path = '2025\day02\inputTest.txt'

with open(path) as file:
    input = file.read()

inputList = re.split(r',|\s', input)

if inputList[-1] == '\n':
    inputList.pop()

print(inputList)

IdList = []

for IdRange in inputList:
    print()
    print(IdRange)
    print()

    rangeList = IdRange.split('-')
    rangeLow = int(rangeList[0])
    rangeHigh = int(rangeList[1])
    rangeLowLen = len(str(rangeLow))
    rangeHighLen = len(str(rangeHigh))

    for sequenceLen in range(1, math.ceil(rangeLowLen/2)):

        print(f'Sequence length: {sequenceLen}')

        sequenceStart = int(str(rangeLow)[0:sequenceLen])

        sequenceEnd = int(str(rangeHigh)[0:sequenceLen])

        for sequence in range(sequenceStart, sequenceEnd + 1):

            sequenceTemp1 = int(str(sequence)*math.floor(rangeLowLen/sequenceLen))
            sequenceTemp2 = int(str(sequence)*(math.floor(rangeLowLen/sequenceLen) + 1))

            if rangeLow <= sequenceTemp1 <= rangeHigh:
                IdList.append(sequenceTemp1)

            if rangeLow <= sequenceTemp2 <= rangeHigh:
                IdList.append(sequenceTemp2)


print(IdList)