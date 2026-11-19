path = '2024\day04\input.txt'

with open(path) as file:
    data = file.read().splitlines()


XMax = len(data[0])
YMax = len(data)



count = 0

for line in range(1, len(data) - 1):
    for pos in range(1, len(data[line]) - 1):

        if data[line][pos] == 'A':

            if data[line-1][pos-1] == 'M' and data[line+1][pos+1] == 'S' or data[line-1][pos-1] == 'S' and data[line+1][pos+1] == 'M':

                if data[line+1][pos-1] == 'M' and data[line-1][pos+1] == 'S' or data[line+1][pos-1] == 'S' and data[line-1][pos+1] == 'M':
                    count += 1



print(f'Solution: {count}')