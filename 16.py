import re

sue = {"children": 3, "cats": 7, "samoyeds": 2 ,"pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

with open("16_input.txt") as f:
  for line in f:
      m = re.search(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line)
      sue_num = m.group(1)
      if sue[m.group(2)] != int(m.group(3)):
        continue
      if sue[m.group(4)] != int(m.group(5)):
        continue
      if sue[m.group(6)] != int(m.group(7)):
        continue
      print "Candidate:",sue_num
