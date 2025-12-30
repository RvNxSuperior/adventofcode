from rich import print

for i in range(9, -1, -1):
    #print(i)
    pass



def getJoltage(bank, min, max):

    OutputJoltage = None
    OutputPosition = None
    joltage = 9

    while OutputJoltage == None and joltage >= 0:
        
        position = min

        while OutputJoltage == None and position <= max:

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

        string = '[white]' + bank[:RangeMax] + '[black]' + bank[RangeMax:]

    else:

        string = '[black]' + bank[:RangeMin] + '[white]' + bank[RangeMin:RangeMax] + '[black]' + bank[RangeMax:]

    print(string)


print(getJoltage('3616433333424364342231322772322273742562435322524343222733733633315231217432253332344435423437477333', 0, 99))

dic = {'A':1, 'B':2}

print(dic.keys())

dic2 = {}

print(type(dic2))

for entry in dic:

    print(entry)

print(dic.keys())
print(type(dic.keys()))

print()

print('Test [black]Test [white]Test')


printBank('3616433333424364342231322772322273742562435322524343222733733633315231217432253332344435423437477333', 50, 90)