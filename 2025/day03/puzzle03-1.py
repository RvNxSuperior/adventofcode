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


    #getting first highest joltage
    firstJoltage = None
    firstPos = None

    for joltage in range(9, -1, -1):

        if firstJoltage == None and firstPos == None:

            for position in range(bankLen):

                if firstJoltage == None and firstPos == None:

                    positionJoltage = int(str(bank)[position])

                    if positionJoltage == joltage:

                        firstJoltage = joltage
                        firstPos = position

    print(f'Joltage 1: {firstJoltage}')
    print(f'Position 2: {firstPos}')
                        
    
    #getting highest or second highest after the first highest
    if firstPos != bankLen - 1:
        secondJoltage = None
        secondPosition = None

        if secondJoltage == None and secondPosition == None:

            for joltage in range(firstJoltage, -1, -1):

                for position in range(firstPos + 1, bankLen):

                    if secondJoltage == None and secondPosition == None:

                        positionJoltage = int(str(bank)[position])

                        if positionJoltage == joltage:

                            secondJoltage = joltage
                            secondPosition = position

        print()
        print(f'Joltage 2: {secondJoltage}')
        print(f'Position 2: {secondPosition}')

        outputJoltage = int(str(firstJoltage) + str(secondJoltage))
            




    elif firstPos == bankLen - 1:
        secondJoltage = None
        secondPosition = None

        for joltage in range(firstJoltage - 1, -1, -1):

            if secondJoltage == None and secondPosition == None:

                for position in range(bankLen - 1):

                    if secondJoltage == None and secondPosition == None:

                        positionJoltage = int(str(bank)[position])

                        if positionJoltage == joltage:

                            secondJoltage = joltage
                            secondPosition = position

        outputJoltage = int(str(secondJoltage) + str(firstJoltage))
    
                            


    else:
        print('ERROR. WTF just happened?')

    joltageList.append(outputJoltage)


sum = 0
print(joltageList)
for joltage in joltageList:
    sum += joltage

print()
print(f'Sum: {sum}')


    

# TODO: change my weird if-statement and for-loop constructs to while loops with implemented counting