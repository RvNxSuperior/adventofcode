

path = '2024/day02/input.txt'

with open(path) as file:
    data = file.read().splitlines()




# processing

reportList = []

for report in data:
    levels = report.split()
    difList = []
    
    for index in range(len(levels) - 1):
        difference = int(levels[index + 1]) - int(levels[index])
        difList.append(difference)

    reportList.append(difList)

safeReports = 0

for entry in reportList:
    print(entry, end=': ')
    if not any(n < -3 or n > 3 or n == 0 for n in entry):

        if entry[0] > 0:
            if not any(n < 0 for n in entry):
                safeReports += 1
                print('safe 1')

            else:
                print('unsafe 2')

        else:
            if not any(n > 0 for n in entry):
                safeReports += 1
                print('safe 2')

            else:
                print('unsafe 3')

    else:
        print('unsafe 1')

            

print(f'Reports: {len(reportList)}')
print(f'Solution: {safeReports}')