import os

path = '2025\day04\input.txt'

with open(path) as file:

    input = file.read()

inputList = input.splitlines()

inputHeight = len(inputList)
inputWidth = len(inputList[0])

print(f'Height: {inputHeight}')
print(f'Width: {inputWidth}')


# this is ugly, I know. I wrote this function half an hour before midnight. Which isn't really that late, but I need excuses for it.
def evaluate(input, row, column):

    sum = 0

    substringList = []

    if row == 0 and column == 0:
        substringList.append(input[row][column+1])
        substringList.append(input[row+1][column:column+2])

    elif column == 0 and row != 0 and row != inputHeight - 1:
        substringList.append(input[row-1][column:column+2])
        substringList.append(input[row][column+1])
        substringList.append(input[row+1][column:column+2])

    elif row == inputHeight - 1 and column == 0:
        substringList.append(input[row-1][column:column+2])
        substringList.append(input[row][column+1])

    elif row == inputHeight - 1 and column != 0 and column != inputWidth - 1:
        substringList.append(input[row-1][column-1:column+2])
        substringList.append(input[row][column-1])
        substringList.append(input[row][column+1])

    elif row == inputHeight - 1 and column == inputWidth - 1:
        substringList.append(input[row-1][column-1:column+1])
        substringList.append(input[row][column-1])

    elif column == inputWidth - 1 and row != 0 and row != inputHeight - 1:
        substringList.append(input[row-1][column-1:column+1])
        substringList.append(input[row][column-1])
        substringList.append(input[row+1][column-1:column+1])

    elif row == 0 and column == inputWidth - 1:
        substringList.append(input[row][column-1])
        substringList.append(input[row+1][column-1:column+1])

    elif row == 0 and column != 0 and column != inputWidth -1:
        substringList.append(input[row][column-1])
        substringList.append(input[row][column+1])
        substringList.append(input[row+1][column-1:column+2])

    else:

        substringList.append(input[row-1][column-1:column+2])
        substringList.append(input[row][column-1])
        substringList.append(input[row][column+1])
        substringList.append(input[row+1][column-1:column+2])

    #I put the substrings in a list and count them here instead of counting them immediately. Don't ask me why. I don't know either
    for substring in substringList:
        sum += substring.count('@')

    return sum



sum = 0
paperCount = 0
emptyCount = 0

threshold = 4

for row in range(inputHeight):
    print()
    print(f'Row:{row}')
    line = inputList[row]
    print(line)

    for column in range(inputWidth):
        print(f'Column:{column:<3} {line[column]} ', end='')

        if line[column] == '@':
            paperCount += 1

            temp = evaluate(inputList, row, column)
            print(f'{temp} ', end='')

            if temp < threshold:

                sum += 1
                print(sum)

            else:
                print()

        else:
            emptyCount += 1
            print()


print()
print(f'Sum: {sum}')
print()
print(f'Paper count: {paperCount}')
print(f'Empty count: {emptyCount}')
print(f'Spaces (computed): {inputHeight * inputWidth}')
print(f'Spaces (counted): {paperCount + emptyCount}')