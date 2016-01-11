import re
import json
import collections

def parse_element(e):
  if type(e) is dict:
    if "red" in e.values():
      return 0
    return parse_element(list(e.values()))
  elif type(e) is list:
    return sum([parse_element(f) for f in e])
  elif type(e) is int:
    return e
  else:
    #print e
    return 0

with open("12_input.txt") as f:
  input = f.readlines()

for line in input:
  obj = json.loads(line)
  #print "Element: %s, Type: %s" %(y, type(y))
  print "Sum: ", parse_element(obj)
