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


# processing

score = 0

for entry in list1:
    print(entry, end=': ')

    subscore = 0

    for entry2 in list2:
        if entry == entry2:
            subscore += 1

    print(subscore)
    score += entry * subscore

print(score)

