file = open("input", 'r')
totalSet = file.read().split("\n")
file.close()

numSet = int(len(totalSet)/2)

file = open("output", "w")
for x in range(numSet):
    pattern = totalSet[x]
    text = totalSet[x+1]
    print(pattern)
    print(text)

    for y in range(0, len(text) - len(pattern) + 1):
        count = 0

        while count < len(pattern) and text[y + count] == pattern[count]:
            count += 1

        if len(pattern) == count:
            file.write(str(y) + " ")
    file.write("\n")
file.close()

