path = '2024\day04\input.txt'

with open(path) as file:
    data = file.read().splitlines()


XMax = len(data[0])
YMax = len(data)



count = 0

for line in range(len(data)):
    for pos in range(len(data[line])):
        top = False
        bottom = False
        right = False
        left = False

        if data[line][pos] == 'X':

            if line < 3:
                top = True

            if line > XMax - 4:
                bottom = True

            if pos < 3:
                left = True

            if pos > YMax - 4:
                right = True

            if top == False and right == False:
                if data[line][pos] == 'X' and data[line-1][pos+1] == 'M' and data[line-2][pos+2] == 'A' and data[line-3][pos+3] == 'S':
                    count += 1

            if right == False:
                if data[line][pos] == 'X' and data[line][pos+1] == 'M' and data[line][pos+2] == 'A' and data[line][pos+3] == 'S':
                    count += 1

            if bottom == False and right == False:
                if data[line][pos] == 'X' and data[line+1][pos+1] == 'M' and data[line+2][pos+2] == 'A' and data[line+3][pos+3] == 'S':
                    count += 1

            if bottom == False:
                if data[line][pos] == 'X' and data[line+1][pos] == 'M' and data[line+2][pos] == 'A' and data[line+3][pos] == 'S':
                    count += 1

            if bottom == False and left == False:
                if data[line][pos] == 'X' and data[line+1][pos-1] == 'M' and data[line+2][pos-2] == 'A' and data[line+3][pos-3] == 'S':
                    count += 1

            if left == False:
                if data[line][pos] == 'X' and data[line][pos-1] == 'M' and data[line][pos-2] == 'A' and data[line][pos-3] == 'S':
                    count += 1

            if top == False and left == False:
                if data[line][pos] == 'X' and data[line-1][pos-1] == 'M' and data[line-2][pos-2] == 'A' and data[line-3][pos-3] == 'S':
                    count += 1

            if top == False:
                if data[line][pos] == 'X' and data[line-1][pos] == 'M' and data[line-2][pos] == 'A' and data[line-3][pos] == 'S':
                    count += 1


print(f'Solution: {count}')