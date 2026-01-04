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