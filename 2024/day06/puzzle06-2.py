import re

path = '2024/day06/input.txt'

with open(path) as file:
    data = file.read().splitlines()

x = None

for y in range(len(data)):

    x = re.search('\\^', data[y])


    if x != None:
        break

x = x.start()

print(f'X: {x}')
print(f'Y: {y}')

XMax = len(data[0])
YMax = len(data)

print(f'Max Y: {YMax}')
print(f'Max X: {XMax}')



# preprocessing first run

# direction 0-3, clockwise, beginning with 12 o'clock = 0
direction = 0

initPath = []

done = False

while done == False:

    if direction == 0 and y > 0:
        newx = x
        newy = y-1

    elif direction == 1 and x < XMax-1:
        newx = x+1
        newy = y

    elif direction == 2 and y < YMax-1:
        newx = x
        newy = y+1

    elif direction == 3 and x > 0:
        newx = x-1
        newy = y

    else: 
        done = True

    if data[newy][newx] != '#':

        initPath.append([x, y, direction])
        x = newx
        y = newy

        #print(f'{x}-{y}')

    else:
        direction = (direction + 1) % 4
        #print(direction)



# processing

count = 0

for positionIndex in range(1, len(initPath)):
    pass
    position = initPath[positionIndex]
    yTemp = position[1]
    xTemp = position[1]
    PathTemp = initPath[:positionIndex-1]

    dataTemp = data.copy()
    dataTemp[yTemp] = data[yTemp][:xTemp] + 'O' + data[yTemp][xTemp+1:]

    




# idea: record all positions and directions in the run without obstacles
# Add obstacles only on the path, because others wouldn't be hit obviously
# detect a loop by checking if the resulting path involves a position which is already known (same coordinates and same orientation)
