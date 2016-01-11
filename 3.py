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
santa = Point(0,0)
robo = Point(0,0)
houses.add(copy.copy(santa))
with open('3_input.txt', 'r') as f:
  robo_move=False
  for line in f:
    for direction in line:
      if direction == '^':
        if robo_move:
          robo.shift(0,1)
        else:
          santa.shift(0,1)
      if direction == 'v':
        if robo_move:
          robo.shift(0,-1)
        else:
          santa.shift(0,-1)
      if direction == '>':
        if robo_move:
          robo.shift(1,0)
        else:
          santa.shift(1,0)
      if direction == '<':
        if robo_move:
          robo.shift(-1,0)
        else:
          santa.shift(-1,0)
      if robo_move:
        p = copy.copy(robo)
        houses.add(p)
      else:
        p = copy.copy(santa)
        houses.add(p)
      robo_move = not robo_move
      print "Adding %s" % p

print "Houses: %s" % houses
print "Total: %s" % len(houses)

