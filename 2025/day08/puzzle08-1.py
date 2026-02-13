import os
import math

path = '2025\day08\input.txt'

with open(path) as file:

    Input = file.read()

InputLines = Input.splitlines()

coordinates = []


# functions

# is maybe equivalent to math.dist()
def distance(list1, list2):

    dist = round(math.sqrt((list1[0] - list2[0])*2 + (list1[1] - list2[1])*2 + (list1[2] - list2[2])*2))

    return dist





# preprocessing

for line in InputLines:

    coordinatesTemp = line.split(',')

    coordinates.append([int(coordinatesTemp[0]), int(coordinatesTemp[1]), int(coordinatesTemp[2])])

XHigh = 0
YHigh = 0
ZHigh = 0

for entry in coordinates:

    if entry[0] > XHigh:
        XHigh = entry[0]

    if entry[1] > XHigh:
        YHigh = entry[2]

    if entry[2] > XHigh:
        ZHigh = entry[2]


print(f'Highest X: {XHigh}')
print(f'Highest Y: {YHigh}')
print(f'Highest Z: {ZHigh}')
print()



chunks = {}

for entry in coordinates:
    # won't work cause it only stores the last list, and not a list of all lists
    # fix asap!!!
    chunks.update({f'{math.floor(entry[0]/5000)}-{math.floor(entry[1]/5000)}-{math.floor(entry[2]/5000)}':entry})

print(coordinates)
print()
print(chunks)




# calculation

MinDistance = None

for entry1 in coordinates:

    print(f'Type Entry 1: {type(entry1)}')

    chunk = [math.floor(entry1[0]/5000), math.floor(entry1[1]/5000), math.floor(entry1[2]/5000)]

    MinDistance = None

    for entry2 in chunks[f'{chunk[0]}-{chunk[1]}-{chunk[2]}']:

        print(f'Type Entry 2: {type(entry2)}')

        dist = distance(entry1, entry2)

        # no check for same distance yet!
        if 0 < dist < MinDistance or MinDistance == None:

            MinDistance = dist

    print(f'{entry1 :<12}: {MinDistance}')