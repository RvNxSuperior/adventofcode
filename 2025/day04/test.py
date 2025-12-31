path = '2025\day04\input.txt'

with open(path) as file:

    input = file.read()

inputList = input.splitlines()

print(f'rows: {len(inputList)}')
print(f'columns: {len(inputList[0])}')

test1 = 1
test2 = 2
test = 'Test'

print(test.count('t'))

row = 1
column = 1

newRow = inputList[row][:column] + 'X' + inputList[row][column + 1:]

print(inputList[row])
print(newRow)