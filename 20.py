import math

def sum_presents(n):
  sumf = 0
  for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
      sumf += i
      sumf += n/i
  print "sum:",sumf
  return sumf*10


house=30000
min_presents = 34000000
while sum_presents(house) < min_presents:
  house += 1

print "House:", house
