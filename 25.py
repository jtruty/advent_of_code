
seed = 20151125
row = 1
max_row = 1
col = 1
while True:
  if row == 1:
    max_row += 1
    row = max_row
    col = 1
  else:
    row -= 1
    col += 1
  seed = (seed * 252533) % 33554393
  if row == 3010 and col == 3019:
    break
print "Row: %s, Col: %s, Num: %s" % (row, col, seed)
