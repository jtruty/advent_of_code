import itertools

total = 150
nums = []
with open("17_input.txt") as f:
  for line in f:
      nums.append(int(line))

perms = []
count = 0
for i in range(1, 5):
  for it in itertools.combinations(nums, i):
    if sum(it) == total:
      print it
      count += 1
print "Count: ", count
