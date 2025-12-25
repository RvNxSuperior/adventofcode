import os
import re
import math

path = '2025\day02\input.txt'

# dictionary of primes for each length without the length itself. Functions as length for each block
primeDic = {1:[1], 2:[1], 3:[1], 4:[1, 2], 5:[1], 6:[1, 2, 3], 7:[1], 8:[1, 2, 4], 9:[1, 3], 10:[1, 2, 5]}

with open(path) as file:
    input = file.read()

inputList = re.split(r',|\s', input)

if inputList[-1] == '\n':
    inputList.pop()

print(inputList)

IdSet = set()

for IdRange in inputList:
    print()
    print(f'ID range: {IdRange}')

    rangeList = IdRange.split('-')
    rangeLow = int(rangeList[0])
    rangeHigh = int(rangeList[1])
    rangeLowLen = len(str(rangeLow))
    rangeHighLen = len(str(rangeHigh))

    if rangeLowLen == rangeHighLen:

        for sequenceLen in primeDic[rangeLowLen]:

            sequenceStart = int(str(rangeLow)[0:sequenceLen])
            sequenceEnd = int(str(rangeHigh)[0:sequenceLen])

            print()
            print(f'Sequence length: {sequenceLen}')
            print(f'Sequence start: {sequenceStart}')
            print(f'Sequence end: {sequenceEnd}')
            print()



            for sequence in range(sequenceStart, sequenceEnd + 1):

                sequenceTemp = int(str(sequence) * int(rangeLowLen/sequenceLen))

                if rangeLow <= sequenceTemp <= rangeHigh:

                    IdSet.add(sequenceTemp)

                    #print(f'ID: {sequenceTemp}')



    else:

        #sequence building for low sequence start to end of low length
        for sequenceLen in primeDic[rangeLowLen]:

            print()
            print(f'Sequence length: {sequenceLen}')
            print(f'Sequence start: {sequenceStart}')
            print(f'Sequence end: {sequenceEnd}')
            print()


        #sequence building for start of high length to end of high sequence
        for sequenceLen in primeDic[rangeHighLen]:
            pass




    



    #for sequenceLen in range(1, math.ceil(rangeLowLen/2) + 1):

        #print(f'Sequence length: {sequenceLen}')

        #sequenceStart = int(str(rangeLow)[0:sequenceLen - rangeLowLen])

        #sequenceEnd = int(str(rangeHigh)[0:sequenceLen - rangeLowLen])

        #print(sequenceStart)
        #print(sequenceEnd)

        #for sequence in range(sequenceStart, sequenceEnd + 1):

            #sequenceTemp1 = int(str(sequence)*math.floor(rangeLowLen/sequenceLen))
            #sequenceTemp2 = int(str(sequence)*(math.floor(rangeLowLen/sequenceLen) + 1))

            #if rangeLow <= sequenceTemp1 <= rangeHigh:
                #IdList.append(sequenceTemp1)

            #if rangeLow <= sequenceTemp2 <= rangeHigh:
                #IdList.append(sequenceTemp2)


print(IdSet)

sum = 0

for Id in IdSet:
    sum += Id


print(f'Sum: {sum}')