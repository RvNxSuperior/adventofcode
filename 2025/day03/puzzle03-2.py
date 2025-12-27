import os

path = '2025\day03\input.txt'

with open(path) as file:
    input = file.read()

inputList = input.splitlines()

count = 0

joltageList = []

for bank in inputList:
    count += 1

    bankLen = len(str(bank))

    print()
    print(f'Bank {count}')
    print(bank)
    print()

    