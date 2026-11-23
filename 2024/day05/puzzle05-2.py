path = '2024/day05/input.txt'

with open(path) as file:
    data = file.read()


# functions

def check(update):
    output = False
    length = len(update)

    for i in range(1, length):
        pageNum = update[i]
        before = update[:i]
        beforeSet = set(before)

        #print(update, end=' - ')
        #print(i, end=' - ')
        #print(pageNum, end=' - ')
        #print(before)

        if pageNum in rulesDict:
            if not beforeSet.isdisjoint(rulesDict[pageNum]):
                output = i
                break

    if output == False:
        output = -1

    
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
    output = 0
    count = 0

    while output >= 0:

        count += 1
        output = check(updateTemp)


        if output > 0:

            outlier = updateTemp[output]

            rule = rulesDict[outlier]

            for i in range(output):

                if updateTemp[i] in rule:

                    #insertion sort
                    updateTemp.insert(i, outlier)
                    updateTemp.pop(output + 1)

                    #bubble sort
                    #updateTemp.insert(i, outlier)
                    #updateTemp.pop(output + 1)
                    #updateTemp.insert(output + 1, updateTemp[i + 1])
                    #updateTemp.pop(i + 1)

                    break

        elif count > 1:
            #print(updateCount, end=': ')
            #print(check(updateTemp), end=' - ')
            #print(update, end=' - ')
            #print(updateTemp)
            
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

# not: 5360 (bubble-sort)
# not: 5228 (wrong sorting)
# not: 5652 (insertion sort)
# not: 3514 (idk where that came from haha)
# probably error with the sorting algorithm, review later!
# ok, reviewed now. Error is definitely in the check-function. Both sorting algorithms produce different sorted lists. Both being verified as valid by the algorithm for some reason. At least one of them being wrong
# fuck, I found my mistake. For some dumb reason, I did not know that in Python, 1 is equal to True. Therefore my funcion, which returns either True, False or the index, did indeed sometimes return 1
# holy shit, this is a fucking mess now from all my fucking around. Gotta fix that at some time. Therefore, in this spririt:
# todo: fix