#!/usr/local/bin/python
import re

def part1():
  count = 0
  with open('5_input.txt', 'r') as f:
    for line in f:
      #if re.match(r'[aeiou]{3,}',line) and re.search(r'([a-z])\1',line) and (re.search(r'(ab|cd|pq|xy)',line) == None):
      if re.search(r'(.*[aeiou].*){3,}',line):
        #print line
        if re.search(r'([a-z])\1',line):
          #print line
          if (re.search(r'(ab|cd|pq|xy)',line) == None):
            print line
            count = count + 1

  print "Count: %s" % count

def part2():
  count = 0
  with open('5_input.txt', 'r') as f:
    for line in f:
      #if re.match(r'[aeiou]{3,}',line) and re.search(r'([a-z])\1',line) and (re.search(r'(ab|cd|pq|xy)',line) == None):
      if re.search(r'(\w{2}).*\1',line):
        #print line
        if re.search(r'(\w)\w\1',line):
          print line
          count = count + 1

  print "Count: %s" % count

part2()
