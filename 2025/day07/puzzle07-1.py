import os

path = '2025\day07\input.txt'

with open(path) as file:

    input = file.read()

inputLines = input.splitlines()

SPosition = len(inputLines[0].split('S')[0])


def findall(string, substring):

    deltaString = 1
    output = []

    start = string.find(substring)

    while deltaString > 0:

        deltaString = 0

        start = string.find(substring, start)

        if start != -1:

            output.append(start)
            deltaString += 1
            start += len(substring)

        
    return output



# preprocessing
print(f'Lines: {len(inputLines)}')
print(f'Width: {len(inputLines[0])}')
print(f'Position S: {SPosition}')

emptyLines = 0

lineCount = 0

for line in inputLines:

    if len(line.split('^')) == 0:

        emptyLines += 1

        if lineCount % 2 != 0:

            print(f'odd empty line in line {lineCount}')


    lineCount += 1



# computing beam

beamSet = {SPosition}

for line in range(2, len(inputLines), 2):

    splitters = findall(inputLines[line], '^')

    print(splitters)