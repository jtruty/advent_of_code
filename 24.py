import itertools

packages = []
with open("24_input.txt") as f:
  for line in f:
    packages.append(int(line.strip()))


target_weight = sum(packages)/4
max_group_size = 8
qe=99999999999999
for i in range(1,max_group_size):
  for combo in itertools.combinations(reversed(packages), i):
    print combo
    if sum(combo) == target_weight:
      qe = min(qe, reduce(lambda a,b: a*b, list(combo)))
print "Min QE: ", qe
