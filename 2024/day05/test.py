test = [1, 2]

test2 = test
test2.pop(1)

print(test)

path = '2024/day05/input.txt'

with open(path) as file:
    data = file.read()



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

num = 0

for update in updates:

    sol = check(update)

    if sol == True:
        num += update[int(len(update)/2)]


print(f'Solution: {num}')


for i in range(10, 1, -1):
    print(i)

    print(len(test))