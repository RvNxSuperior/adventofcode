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

print()
print(f'Highest X: {XHigh}')
print(f'Highest Y: {YHigh}')
print(f'Highest Z: {ZHigh}')
print()



chunks = {}

for entry in coordinates:
    # won't work cause it only stores the last list, and not a list of all lists
    # fix asap!!!

    chunk = f'{math.floor(entry[0]/5000)}-{math.floor(entry[1]/5000)}-{math.floor(entry[2]/5000)}'

    if chunk in chunks:
        chunks[chunk].append(entry)

    else:
        chunks.update({chunk:[entry]})

#print(coordinates)
#print()
#print(chunks)




# calculating distances of all combinations

print('Calculating distances for all coordinate combinations')

Distances = {}


# currentyl gives the same answer multiple times if two points are to eachother the closest
for entry1 in coordinates:

    #chunk = [math.floor(entry1[0]/5000), math.floor(entry1[1]/5000), math.floor(entry1[2]/5000)]

    #MinDistance = None

    for entry2 in coordinates:

        dist = math.dist(entry1, entry2)

        if dist > 0 and frozenset({str(entry1), str(entry2)}) not in Distances:

            Distances.update({frozenset({str(entry1), str(entry2)}):dist})


# iterate through dictionary and check the partner if it's a double entry
# idea: use frozenset instead of string as key in dictionary to prevent duplicates
# see: https://stackoverflow.com/questions/59933892/set-as-dictionary-key

print()
print(f'Calculated maximum entries: {(len(InputLines))**2 - len(InputLines)}')
print(f'Number of entries: {len(Distances)}')





# ordering coordinate combinations by ascending distance

print('Ordering coordinate combinations by ascending distance')

DistancesSorted = sorted(Distances.items(), key=lambda x:x[1])


ConnectionCount = 1000

# getting x shortest connections

for connection in range(ConnectionCount):

    pass


CountedCircuits = 3

# multiplying the lengths of the y longest circuits



## ideas ##
# first loop through all pairs of coordinates and find all distances
# then sort by length
# in a second step go through the first 1000 shortest distances and combine sets of the coordinates
# maybe later: compute distances wit chunks to ensure not computing all points
# maybe later 2: compute distances with chunks