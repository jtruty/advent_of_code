import re
from collections import defaultdict

input_seq = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

def part1():
  input = []
  with open("19_input.txt") as f:
    input = f.readlines()

  total_sets = set()
  for line in input:
    molecules = line.split(" => ")
    if len(molecules) == 2:
      charToFind = molecules[0].strip()
      print charToFind
      replacement = molecules[1].strip()
      print replacement
      for match in re.finditer(charToFind, input_seq):
        print "Match: ", match.start(), match.group(0)
        replaced = input_seq[:match.start()] + replacement + input_seq[match.end():]
        total_sets.add(replaced)
        print "Replacement: ", replaced

  print len(total_sets)

def part2():
  input = set() # map of seq to seq to replace
  with open("19_input.txt") as f:
    for line in f:
      molecules = line.split(" => ")
      if len(molecules) == 2:
        input.add(molecules[0])

  el_count = 0
  paren_count = 0
  comma_count = 0
  matches = re.findall(r'[A-Z][a-z]?', input_seq)
  for i, j in enumerate(matches):
    if j == "Rn" or j == "Ar":
      paren_count += 1
    if j == "Y":
      comma_count += 1

  total = len(matches) - paren_count - 2*comma_count - 1
  print total

part2()


