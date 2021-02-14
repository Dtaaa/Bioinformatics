file = open("input", 'r')
totalSet = file.read().split("\n")
file.close()


file = open("output", "w")

for seq in totalSet:
    result = []
    skewList = []
    position = 0

    for y in seq:
        if 'C' == y:
            position -= 1
        elif 'G' == y:
            position += 1
        skewList.append(position)

    if len(skewList) > 0:
        minimum = min(skewList)
        for i in range(len(skewList)):
            if skewList[i] == minimum:
                result.append(i + 1)

    for y in result:
        file.write(str(y) + " ")

    file.write("\n")


file.close()
