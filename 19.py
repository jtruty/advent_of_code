import re

input_seq = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
total_sets = set()
with open("19_input.txt") as f:
  for line in f:
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
