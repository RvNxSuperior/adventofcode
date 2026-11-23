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










# idea: record all positions and directions in the run without obstacles
# Add obstacles only on the path, because others wouldn't be hit obviously
# detect a loop by checking if the resulting path involves a position which is already known (same coordinates and same orientation)
