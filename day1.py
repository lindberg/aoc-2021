with open('inputs/day1.txt') as f:
    lines = [int(line) for line in f.read().split("\n")]

count = 0

for i in range(3, len(lines)):
    sum1 = lines[i-3] + lines[i-2] + lines[i-1]
    sum2 = lines[i-2] + lines[i-1] + lines[i]

    if sum2 > sum1:
        count += 1

print(count)
