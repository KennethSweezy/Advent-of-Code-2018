total = 0

input = open('C:\Users\Kenneth\Documents\GitHub\Advent-of-Code-2018\Day01\Part 1\input.txt', 'r')
for line in input:
    if "+" in line:
        currentLine = line
        truncatedLine = line[1:]
        lineVal = int(truncatedLine)
        total = total + lineVal
    elif "-" in line:
        currentLine = line
        truncatedLine = line[1:]
        lineVal = int(truncatedLine)
        total = total - lineVal
print(total)