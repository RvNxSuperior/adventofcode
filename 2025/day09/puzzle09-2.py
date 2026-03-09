import os
import math

path = '2025/day09/input.txt'

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
MaxX = None
MinX = None
MaxY = None
MinY = None

for line in InputLines:

    split = line.split(',')

    coordinates.append([int(split[0]), int(split[1])])

    if MaxX == None or int(split[0]) > MaxX:
        MaxX = int(split[0])

    elif MinX == None or int(split[0]) < MinX:
        MinX = int(split[0])

    if MaxY == None or int(split[1]) > MaxY:
        MaxY = int(split[1])

    elif MinY == None or int(split[1]) < MinY:
        MinY = int(split[1])

print(f'Minimum X: {MinX}')
print(f'Maximum X: {MaxX}')
print(f'Minimum Y: {MinY}')
print(f'Maximum Y: {MaxY}')
print()


# calculating full grid based on coordinates

grid = []
orientation = 0

# initialize empty grid
for height in range(MaxY):

    grid.append('.'*MaxX)




for connectionIndex in range(len(coordinates) - 1):

    coordinate1 = coordinates[connectionIndex]
    coordinate2 = coordinates[connectionIndex + 1]

    if coordinate1[0] == coordinate2[0]:
        pass

    elif coordinate1[1] == coordinate2[1]:
        grid[coordinate1[1]] = grid[coordinate1[1]]

    else:
        print('Error, unexpected input')



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


# notes: checks any possible rectangle for validity by searching for red tiles (given coordinates)
# in the rectangle inscribed by the possible rectangle
# won't work correctly when lines go through the inscribed rectangle without the coordinates being inside it

# idea 1:
# mostly preprocessing-heavy
# compute the full grid of red, green and uncoloured tiles from the coordinates
# then check for uncoloured tiles when checking for validity

# idea 2:
# mostly processing-heavy
# precompute all lines between the coordinates and check for red tiles or the lines between them when checking for validity
