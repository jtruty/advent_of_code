import re

sue = {"children": 3, "cats": 7, "samoyeds": 2 ,"pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

with open("16_input.txt") as f:
  for line in f:
    m = re.search(r'Sue (\d+): (\w+: \d+), (\w+: \d+), (\w+: \d+)', line)
    sue_num = m.group(1)
    possible = True
    for i in range(2,5):
      match = m.group(i).split(": ")
      thing = match[0]
      num = int(match[1])
      if thing == "cats" or thing == "trees":
        if sue[thing] >= num:
          possible = False
      elif thing == "pomeranians" or thing == "goldfish":
        if sue[thing] < num:
          possible = False
      else:
        if sue[thing] != num:
          possible = False
    if possible:
      print "Candidate:",sue_num
