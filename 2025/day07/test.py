def findall(string, substring):

    deltaString = 1
    output = []

    start = string.find(substring)

    while deltaString > 0:

        deltaString = 0

        start = string.find(substring, start)

        if start != -1:

            output.append(start)
            deltaString += 1
            start += len(substring)

        
    return output


print(findall('.....................................................................^.^.....................................................................', '^'))

dic = {1:1}
dic[1] += 1
print(dic[1])