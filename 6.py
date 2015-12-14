#!/usr/local/bin/python
import re

lights = [[False]*1000 for i in range(1000)]  #initialize to all 0s
#print lights


def change_coord(action, x, y):
  #print "Changing: %s, %s, %s" % (action, x, y)
  if "off" == action:
    lights[x][y] = False
  elif "on" == action:
    lights[x][y] = True
  elif "toggle" == action:
    if lights[x][y] == True:
      lights[x][y] = False
    else:
      lights[x][y] = True
    #print lights[x][y]

def parse_coords(line):
  m = re.search('(\w+)\s+(\d+),(\d+)\D+(\d+),(\d+)',line)
  action = m.group(1)
  start_x = int(m.group(2))
  start_y = int(m.group(3))
  end_x = int(m.group(4))
  end_y = int(m.group(5))
  #print "Action %s" % action
  #print "Start: %i, %i" % (start_x, start_y)
  #print "End: %i, %i" % (end_x, end_y)
  for x in range(start_x, end_x+1):
    for y in range(start_y, end_y+1):
      change_coord(action, x, y)


with open('6_input.txt', 'r') as f:
  for line in f:
    parse_coords(line)

count = 0
for xel in lights:
  for yel in xel:
    if yel == True:
      count += 1

#print lights
print count
