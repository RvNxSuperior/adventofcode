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

    coordinates.append(line.split(','))


# processing

print('Computing areas of all coordinate combinations...')

Max = 0

for entry1 in coordinates:

    for entry2 in coordinates:

        area = (abs(int(entry1[0]) - int(entry2[0])) + 1) * (abs(int(entry1[1]) - int(entry2[1])) + 1)

        if area > Max:

            Max = area


print()
print(f'Biggest possible area: {Max}')