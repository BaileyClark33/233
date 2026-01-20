startList = [1,3,7,8,66,2,1,4]

floatList = []

for i in range(len(startList)):
    floatList.append(float(startList[i]))

print(floatList)

for i in range(len(startList)):
    print(floatList[i], " ", end="")
    if startList[i] > 3:
        print("BIG", end="")
    print()

evenList = []
oddList = []

for i in range(len(startList)):
    if startList[i] % 2 == 0:
        evenList.append("EVEN")
    else:
        oddList.append("ODD")

print("EVEN: ", len(evenList), " ODD: ", len(oddList))

