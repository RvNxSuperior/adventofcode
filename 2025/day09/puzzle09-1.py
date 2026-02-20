import os
import math

path = '2025\day09\input.txt'

with open(path) as file:

    Input = file.read()

InputLines = Input.splitlines()


# preprocessing

print('Preprocessing...')

coordinates = []

for line in InputLines:

    split = line.split(',')

    coordinates.append([int(split[0]), int(split[1])])


# processing

print('Computing areas of all coordinate combinations...')

Max = 0

for entry1 in coordinates:

    for entry2 in coordinates:

        area = (abs(entry1[0] - entry2[0]) + 1) * (abs(entry1[1] - entry2[1]) + 1)
        
        if area > Max:

            Max = area


print()
print(f'Biggest possible area: {Max}')