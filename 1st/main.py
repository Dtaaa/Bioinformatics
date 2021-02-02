file = open("input", 'r')
text = file.read()
file.close()
output = [0, 0, 0, 0]
DNA = ['A', 'C', 'G', 'T']
count = 0

for x in DNA:
    for temp in text:
        if (x == temp):
            output[count] += 1
    count += 1
file = open("output", "a")
for x in range(0, 4):
    file.write(str(output[x]))
    if (x < 3):
        file.write(" ")

file.close()