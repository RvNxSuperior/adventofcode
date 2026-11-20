path = '2024/day05/input.txt'

with open(path) as file:
    data = file.read()


# functions

def check(update):
    output = True
    length = len(update)
    

    for i in range(1, length):
        pageNum = update[i]
        before = update[:i-1]
        beforeSet = set(before)

        if pageNum in rulesDict:
            if not beforeSet.isdisjoint(rulesDict[pageNum]):
                output = i

    return output


# preprocessing

DataList = data.split('\n\n')

rules = DataList[0].splitlines()
updates = DataList[1].splitlines()

rulesDict = {}

for index in range(len(rules)):
    ruleTemp = rules[index].split('|')

    if int(ruleTemp[0]) in rulesDict:
        rulesDict[int(ruleTemp[0])].add(int(ruleTemp[1]))

    else:
        rulesDict.update({int(ruleTemp[0]) : {int(ruleTemp[1])}})

for index in range(len(updates)):
    updates[index] = updates[index].split(',')

    for i in range(len(updates[index])):
        updates[index][i] = int(updates[index][i])


# processing

numFalse = 0
numCorrect = 0
fails = 0
initCorrect = 0
initFalse = 0
updateCount = 0
updatesCorrect = []

for update in updates:

    updateCount += 1

    updateTemp = update.copy()
    output = False
    count = 0

    while output != True:

        count += 1
        output = check(updateTemp)


        if output != True:

            outlier = updateTemp[output]

            rule = rulesDict[outlier]

            for i in range(output - 1):

                if updateTemp[i] in rule:

                    updateTemp.insert(i, outlier)
                    updateTemp.pop(output + 1)

                    break

        elif count > 1:
            print(check(updateTemp), end=' - ')
            print(count, end=' - ')
            print(len(update), end=' - ')
            print(update, end=' - ')
            print(updateTemp)
            
            numFalse += updateTemp[int(len(updateTemp) / 2)]

            initFalse += 1
            updatesCorrect.append(updateTemp)
            
        else:
            initCorrect += 1
            numCorrect += update[int(len(updateTemp) / 2)]

            updatesCorrect.append(update)



        
print(f'Solution 1: {numCorrect}')
print(f'Solution 2: {numFalse}')
print(f'Initially correct: {initCorrect}')
print(f'Initially false: {initFalse}')
print(f'Sum: {initFalse + initCorrect}')
print(f'Update count: {updateCount}')
