data = []

with open("data.txt") as fileObj:
    data = [long(line.strip()) for line in fileObj]

total = 0
for x in data:
    total = total + x

print total
