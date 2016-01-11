#!/usr/local/bin/python
import re

total_paper = 0
total_ribbons = 0
with open('2_input.txt', 'r') as f:
  for line in f:
    dims = line.split('x')
    dims = [int(i) for i in dims]
    dims.sort()
    l=dims[0]
    w=dims[1]
    h=dims[2]
    sqft = 2*l*w + 2*w*h + 2*h*l + l*w
    sqft_ribbons = l*w*h
    sqft_ribbons += 2*l + 2*w
    total_paper += sqft
    total_ribbons += sqft_ribbons

print "total_paper: %s" % total_paper
print "total_ribbons: %s" % total_ribbons
