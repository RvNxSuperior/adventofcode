import os
import math

path = '2025\day09\input.txt'

with open(path) as file:

    Input = file.read()

InputLines = Input.splitlines()


# functions

def valid(entry1, entry2):

    output = True

    # compute inscribed rectangle x coordinate
    if entry1[0] > entry2[0]:

        inscribedCorner1 = [entry2[0] + 1]
        inscribedCorner2 = [entry1[0] - 1]

    elif entry1[0] < entry2[0]:

        inscribedCorner1 = [entry1[0] + 1]
        inscribedCorner2 = [entry2[0] - 1]

    else:

        return False


    # compute inscribed rectangle y coordinate
    if entry1[1] > entry2[1]:

        inscribedCorner1.append(entry2[1] + 1)
        inscribedCorner2.append(entry1[1] - 1)

    elif entry1[1] < entry2[1]:

        inscribedCorner1.append(entry1[1] + 1)
        inscribedCorner2.append(entry2[1] - 1)

    else:
        
        return False
    

    for check in coordinates:

        if inscribedCorner1[0] <= check[0] <= inscribedCorner2[0] and inscribedCorner1[1] <= check[1] <= inscribedCorner2[1]:

            output = False



    return output

    


# preprocessing

print()
print('Preprocessing...')

coordinates = []

for line in InputLines:

    split = line.split(',')

    coordinates.append([int(split[0]), int(split[1])])



# processing

print('Processing...')

Max = 0

for entry1Index in range(math.ceil(len(coordinates)/2)):

    entry1 = coordinates[entry1Index]

    for entry2 in coordinates:

        area = (abs(entry1[0] - entry2[0]) + 1) * (abs(entry1[1] - entry2[1]) + 1)

        if area > Max and valid(entry1, entry2) == True:

            Max = area
            MaxEntry1 = entry1
            MaxEntry2 = entry2



print()
print(f'Biggest possible area: {Max}')
print(f'Entry 1: {MaxEntry1}')
print(f'Entry 2: {MaxEntry2}')
print()

