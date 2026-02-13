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


def findleft(start = None):


    if start != None:

        output = start
        startInt = len(start)
        pos = SPosition + start.count('R') - start.count('L')


    else:

        output = ''
        startInt = 0
        pos = SPosition

    
    for stage in range(startInt, int(len(inputLines)/2)):

        if inputLines[stage*2][pos] == '^':

            pos -= 1
            output += 'L'

        else:

            output += '-'

    
    return output

print()
print('Running...')

SolutionSet = set()

seed = findleft()
count = 0


while seed.count('L') > 0 and count <= 100000000:

    count += 1

    lastL = findall(seed, 'L')[-1]

    current = findleft(seed[0:lastL] + 'R')

    SolutionSet.add(current)
    seed = current

    #print(f'{count :<5}: {current}')

    if count % 100000 == 0:
        print(f'{count:<10}: {current}')


print()
print(f'{count :<5}: {current}')
print(f'Solution count: {len(SolutionSet)}')


# ideas: solve problem with depth first search approach
# necessary: 2 functions:
# 1. finding the left-most sequence with a given starting sequence
# 2. finding the deepest splitter which hasn't been turned to a right split previously
# loop finctions and store corresponding results in a set
# CAVE: include spaces with no splitters in the solution to not end up with the same path-name for different paths

# update: computational power is not sufficient for brute-force. Probably better to calculate the paths like in 07-1 but adjust for mutliple rays overlapping.
# Maybe use a dictionary for the paths and multiply