#!/usr/local/bin/python
import re

total = 0
with open('2_input.txt', 'r') as f:
  for line in f:
    dims = line.split('x')
    dims = [int(i) for i in dims]
    dims.sort()
    l=dims[0]
    w=dims[1]
    h=dims[2]
    sqft = 2*l*w + 2*w*h + 2*h*l + l*w
    print sqft
    total = total + sqft

print "Total: %s" % total
