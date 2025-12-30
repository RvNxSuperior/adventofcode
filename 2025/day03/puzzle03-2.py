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

    
# idea: use a function that, similarly to puzzle 03-1, gets the highest joltage in a bank,
# but adjust the range in which the function searches
# meaning that it looks for the highest joltage in the bank excluding the last 11 position, because a joltage there can't be used as the first joltage
# and for every following joltage adjust the range to only search in the span between the joltage before and the joltage which can still be used