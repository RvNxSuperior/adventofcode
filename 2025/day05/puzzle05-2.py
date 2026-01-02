import os

path = '2025\day05\input.txt'

with open(path) as file:

    input = file.read()

inputSplit = input.split('\n\n')

inputRangeList = inputSplit[0].splitlines()
inputIdList = inputSplit[1].splitlines()

inputIdListTemp = []

for id in inputIdList:

    inputIdListTemp.append(int(id))

IdList = sorted(inputIdListTemp)


rangeList = []

# preparsing all ranges
for range in inputRangeList:

    rangeTemp = range.split('-')

    rangeList.append([int(rangeTemp[0]), int(rangeTemp[1])])

rangeList = sorted(rangeList, key=lambda x: x[0])

rangeListLen = len(rangeList)



# combining overlapping ranges

deltaLen = 1

while deltaLen > 0:

    rangeListTemp = []
    count = 0
    rangeListLenTemp = len(rangeList)
    deltaLen = 0

    while count < rangeListLenTemp:
        
        if count < rangeListLenTemp - 1 and rangeList[count][1] + 1 >= rangeList[count + 1][0]:

            if rangeList[count + 1][1] > rangeList[count][1]:
            
                rangeListTemp.append([rangeList[count][0], rangeList[count + 1][1]])

            else:

                rangeListTemp.append([rangeList[count][0], rangeList[count][1]])

            deltaLen += 1
            count += 2

        else:

            rangeListTemp.append(rangeList[count])

            count += 1

    rangeList = rangeListTemp
    

#print(rangeListTemp)
print('parsed ranges')
print(f'Original number of ranges: {rangeListLen}')
print(f'New number of ranges: {len(rangeList)}')


# parse new combined ranges and sum up corresponding range lengths

rangeLen = 0

for range in rangeList:

    #print(range)

    rangeLenTemp = range[1] - (range[0] - 1)

    rangeLen += rangeLenTemp

print()
print(f'Range lengths: {rangeLen}')