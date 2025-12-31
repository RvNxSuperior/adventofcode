import os

path = '2025\day05\input.txt'

with open(path) as file:

    input = file.read()

inputSplit = input.split('\n\n')

inputRangeList = inputSplit[0].splitlines()
inputIdList = inputSplit[1].splitlines()


rangeList = []

# preparsing all ranges
for range in inputRangeList:

    rangeTemp = range.split('-')

    rangeList.append([int(rangeTemp[0]), int(rangeTemp[1])])

rangeList = sorted(rangeList, key=lambda x: x[0])


rangeListTemp = []

count = 0

rangeListLen = len(rangeList)

while count < rangeListLen:
    
    if count < rangeListLen - 1 and rangeList[count][1] > rangeList[count + 1][0]:

        rangeListTemp.append([rangeList[count][0], rangeList[count + 1][1]])

    else:

        rangeListTemp.append(rangeList[count])

    count += 1

print(rangeListTemp)
print(len(rangeListTemp))



# watch out for following constellation in ranges:
# number 1 - number 2
# number 1 - number 3
# with number 2 > number 3