#!/usr/local/bin/python
import copy

class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

houses = set()
point = Point(0,0)
houses.add(copy.copy(point))
with open('3_input.txt', 'r') as f:
  for line in f:
    for direction in line:
      if direction == '^':
        point.shift(0,1)
      if direction == 'v':
        point.shift(0,-1)
      if direction == '>':
        point.shift(1,0)
      if direction == '<':
        point.shift(-1,0)
      p = copy.copy(point)
      houses.add(p)
      print "Adding %s" % p

print "Houses: %s" % houses
print "Total: %s" % len(houses)

