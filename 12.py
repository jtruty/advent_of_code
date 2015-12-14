import re

with open("12_input.txt") as f:
    input = f.readlines()

sum = 0
for line in input:
  for match in re.finditer(r'(-?\d+)', line):
    print match.group(1)
    sum += int(match.group(1))
print "Sum: ", sum
