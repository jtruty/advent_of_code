#!/usr/local/bin/python
import re

floor = 0
letter_index = 0
with open('1_input.txt', 'r') as f:
  for line in f:
    for letter in line:
      if letter == '(':
        floor = floor + 1
      else:
        floor = floor - 1
      if floor == -1:
        print "basement index: ", letter_index + 1
      letter_index += 1


print "Floor: %s" % floor
