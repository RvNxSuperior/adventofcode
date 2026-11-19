path = '2024\day05\input.txt'

with open(path) as file:
    data = file.read()


# preprocessing

DataList = data.split('\n\n')

rules = DataList[0].splitlines()
updates = DataList[1].splitlines()

rulesDict = {}

for index in range(len(rules)):
    ruleTemp = rules[index].split('|')

    if int(ruleTemp[0]) in rulesDict:
        rulesDict[int(ruleTemp[0])] = rulesDict[int(ruleTemp[0])].add(int(ruleTemp[1]))

    else:
        rulesDict.update({int(ruleTemp[0]) : set(int(ruleTemp[1]))})

for index in range(len(updates)):
    updates[index] = updates[index].split(',')


print(rulesDict)

# processing

num = 0

for update in updates:
    length = len(update)

    for i in range(length - 1):
        pass

