import os
from rich import print

path = '2025\day03\input.txt'

with open(path) as file:
    input = file.read()

inputList = input.splitlines()

outputLen = 12




def getJoltage(bank, RangeMin, RangeMax):

    OutputJoltage = None
    OutputPosition = None
    joltage = 9

    while OutputJoltage == None and joltage >= 0:
        
        position = RangeMin

        while OutputJoltage == None and position <= RangeMax:

            positionJoltage = int(bank[position])

            if positionJoltage == joltage:

                OutputJoltage = joltage
                OutputPosition = position

            position += 1

        joltage -= 1

    output = {OutputPosition:OutputJoltage}

    return output


def printBank(bank, RangeMin, RangeMax):

    if RangeMin == 0:

        string = '[white]' + bank[:RangeMax+1] + '[black]' + bank[RangeMax+1:]

    else:

        string = '[black]' + bank[:RangeMin] + '[white]' + bank[RangeMin:RangeMax+1] + '[black]' + bank[RangeMax+1:]

    print(string)




count = 0

joltageList = []

for bank in inputList:
    count += 1

    bankLen = len(str(bank))

    RangeMin = 0
    RangeMax = bankLen - outputLen #keep off-1 error in mind

    outputDic = {}

    print()
    print(f'Bank {count}')
    print(bank)
    print()

    for digit in range(outputLen):

        printBank(bank, RangeMin, RangeMax)

        output = getJoltage(bank, RangeMin, RangeMax)

        RangeMin = list(output.keys())[0] + 1
        RangeMax += 1

        outputDic.update(output)

    print(outputDic)

    joltage = ''

    for entry in outputDic:
        joltage += str(outputDic[entry])

    joltageList.append(int(joltage))



sum = 0

for bankJoltage in joltageList:

    sum += bankJoltage

print()
print(joltageList)
print()
print(f'Sum: {sum}')




    
# idea: use a function that, similarly to puzzle 03-1, gets the highest joltage in a bank,
# but adjust the range in which the function searches
# meaning that it looks for the highest joltage in the bank excluding the last 11 position, because a joltage there can't be used as the first joltage
# and for every following joltage adjust the range to only search in the span between the joltage before and the joltage which can still be used