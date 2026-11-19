

path = '2024/day02/input.txt'

with open(path) as file:
    data = file.read().splitlines()

# functions

def checkReportDif(report):
    output = True
    decreasing = 0

    for index in range(len(report) - 1):
        dif = report[index + 1] - report[index]

        if dif == 0 or dif < -3 or dif > 3:
            output = False

        if index == 0:
            if dif < 0:
                decreasing = True

        else:
            if decreasing == True:
                if dif > 0:
                    output = False

            else:
                if dif < 0:
                    output = False

    return output



# preprocessing

dataProcessed = []

for report in data:
    levels = report.split()

    levelsProcessed = []
    for n in levels:
        levelsProcessed.append(int(n))
    dataProcessed.append(levelsProcessed)



# processing

safeReports = 0

for entry in dataProcessed:
    print(entry)

    if checkReportDif(entry) == True:

        safeReports += 1

    else:

        safeReportTemp = False

        for index in range(len(entry)):
            tempEntry = entry.copy()

            tempEntry.pop(index)

            if checkReportDif(tempEntry) == True:

                safeReportTemp = True

        if safeReportTemp == True:

            safeReports += 1
    





print(f'Reports: {len(dataProcessed)}')
print(f'Solution: {safeReports}')