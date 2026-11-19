import os
import math
from tqdm import tqdm

path = '2025/day09/test.txt'

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

    


# preprocessing 1

print()
print('Preprocessing 1...')

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


# calculating full grid based on coordinates

grid = []
orientation = 0

# initialize empty grid
for height in range(MaxY + 2):

    grid.append('.' * (MaxX + 1))


#for line in grid:
#    print(line)


# preprocessing integrity check 1

defaultLength = len(grid[0])

for i in range(len(grid)):

    if defaultLength != len(grid[i]):

        print(f'Error! (line {i})')
        print('Unexpected preprocessing 1 values!')
        print(f'Default: {defaultLength}')
        print(f'Error: {len(grid[i])}')

        break

    if i == len(grid) - 1:

        print('Preprocessing integrity 1 confirmed')


# preprocessing 2

print('Preprocessing 2...')

for connectionIndex in range(len(coordinates)):

    coordinate1 = coordinates[connectionIndex]
    coordinate2 = coordinates[(connectionIndex + 1) % len(coordinates)]

    if coordinate1[0] == coordinate2[0]:

        if coordinate2[1] > coordinate1[1]:
            
            for line in range(coordinate1[1] + 1, coordinate2[1]):

                grid[line] = grid[line][:coordinate1[0] - 1] + 'X' + grid[line][coordinate1[0] + 1 - 1:]

        elif coordinate2[1] < coordinate1[1]:
            
            for line in range(coordinate2[1] + 1, coordinate1[1]):

                grid[line] = grid[line][:coordinate1[0] - 1] + 'X' + grid[line][coordinate1[0] + 1 - 1:]

    elif coordinate1[1] == coordinate2[1]:

        if coordinate2[0] > coordinate1[0]:

            grid[coordinate1[1]] = grid[coordinate1[1]][:coordinate1[0] - 1] + '@' + 'X' * (coordinate2[0] - coordinate1[0] - 1) + '@' + grid[coordinate1[1]][coordinate2[0] -1 + 1:]


        elif coordinate2[0] < coordinate1[0]:

            grid[coordinate1[1]] = grid[coordinate1[1]][:coordinate2[0] - 1] + '@' + 'X' * (coordinate1[0] - coordinate2[0] - 1) + '@' + grid[coordinate1[1]][coordinate1[0] -1 + 1:]
            

    else:
        print('Error, unexpected input')







# preprocessing integrity test 2

defaultLength = len(grid[0])

for i in range(len(grid)):

    if defaultLength != len(grid[i]):

        print(f'Error! (line {i})')
        print('Unexpected preprocessing 2 values!')
        print(f'Default: {defaultLength}')
        print(f'Error: {len(grid[i])}')

        break

    if i == len(grid) - 1:

        print('Preprocessing integrity 2 confirmed')



# preprocessing 3

print('Preprocessing 3...')

for y in tqdm(range(len(grid))):
    inside = 0
    length = 0
    edgeUp = False
    edge = False

    for x in range(len(grid[y])):

        if grid[y][x] == 'X':

            if inside == 0:

                inside = 1

            elif edge == True:

                pass

            else:

                inside = 0

                grid[y] = grid[y][:x - length + 1] + 'x' * (length - 1) + grid[y][x:]

        elif grid[y][x] == '@':

            if inside == 1 and edge == False:
                grid[y] = grid[y][:x - length + 1] + 'x' * (length - 1) + grid[y][x:]

            if edge == True:

                if edgeUp == True and grid[y-1][x] == 'X':
                    inside = inside ^ 1

                elif edgeUp == False and grid[y+1][x] == 'X':
                    inside = inside ^ 1

                edge = False
                length = 0

            elif grid[y][x + 1] == 'X':

                edge = True

                if grid[y + 1][x] != 'X':

                    edgeUp = True

        elif inside == 1:
            length += 1
            
    




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

for line in grid:
    print(line)


# notes: checks any possible rectangle for validity by searching for red tiles (given coordinates)
# in the rectangle inscribed by the possible rectangle
# won't work correctly when lines go through the inscribed rectangle without the coordinates being inside it

# formatting:
# red tiles (given by coordinates): @
# green tiles (connecting and filling): X
# empty/uncoloured: .

# idea 1:
# mostly preprocessing-heavy
# compute the full grid of red, green and uncoloured tiles from the coordinates
# then check for uncoloured tiles when checking for validity

# idea 2:
# mostly processing-heavy
# precompute all lines between the coordinates and check for red tiles or the lines between them when checking for validity
