test1 = ' '
test2 = ' '
test3 = ' '

if test1 == test2 == test3 == ' ':
    print('True')

test = 2
test *= 2

print(test)



path = '2025\day06\input.txt'

with open(path) as file:

    input = file.read()


inputList = input.splitlines()

print(f'Input lines: {len(inputList)}')