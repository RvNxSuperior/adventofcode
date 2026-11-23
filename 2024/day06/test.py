print(len([1]))

test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(test[:5])
print(test[5:])

x = 0

for i in range(10):
    x = (x+1) % 4
    print(x)