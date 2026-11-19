import os

path = '2024/day01/input.txt'

with open(path) as file:
    data = file.read()

# preprocessing

data = data.splitlines()

list1 = []
list2 = []

for line in data:
    entries = line.split()

    list1.append(int(entries[0]))
    list2.append(int(entries[1]))


list1.sort()
list2.sort()

list3 = []
solution = 0


# processing

for index in range(len(list1)):
    difference = abs(list1[index] - list2[index])
    list3.append(difference)
    solution += difference


print(f'Solution: {solution}')