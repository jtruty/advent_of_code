import re

def getNextPassword(pass_input):
  last_index = len(pass_input) - 1
  pass_next = ""
  while last_index > 0:
    if pass_input[last_index] == 'z':
      pass_next = pass_next + 'a'
      last_index -= 1
    else:
      pass_next = chr(ord(pass_input[last_index])+1) + pass_next
      break
  return pass_input[:last_index] + pass_next


def hasStraightSequence(pass_input):
  return re.search(r'abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz',pass_input)

def allValidChars(pass_input):
  return not re.search(r'[ilo]',pass_input)

def hasPairs(pass_input):
  pairs = set(["aa","bb","cc","dd","ee","ff","gg","hh","jj","kk","mm","nn","pp","qq","rr","ss","tt","uu","vv","ww","xx","yy","zz"])
  pair_count = 0
  index = 0
  while index+1<len(pass_input):
    this_pair = pass_input[index:index+2]
    if this_pair in pairs:
      pairs.discard(this_pair)
      pair_count += 1
      index += 1
    index += 1
  return pair_count > 1

start = "hepxcrrq"

while True:
  next_pass = getNextPassword(start)
  #print "Next Password to test:", next_pass
  if hasStraightSequence(next_pass) and allValidChars(next_pass) and hasPairs(next_pass):
    print "Next Password:", next_pass
    break
  start = next_pass
