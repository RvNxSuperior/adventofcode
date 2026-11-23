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

XMax = len(data[0])
YMax = len(data)

print(f'Max Y: {YMax}')
print(f'Max X: {XMax}')



# direction 0-3, clockwise, beginning with 12 o'clock = 0
direction = 0


# processing

done = False

print(data[129][115])

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

        data[y] = data[y][:x] + 'X' + data[y][x+1:]
        x = newx
        y = newy

        #print(f'{x}-{y}')

    else:
        direction = (direction + 1) % 4
        #print(direction)

count = 0

for y in range(len(data)):

    x = re.findall('X', data[y])

    print(data[y])

    count += len(x)

print(f'Solution: {count}')


# Ok, this is gonna be a lazy attempt. I'm not bothering implementing some kind of fancy data structure
