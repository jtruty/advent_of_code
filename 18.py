from copy import deepcopy

lights = [[0 for x in range(100)] for x in range(100)]
with open("18_input.txt") as f:
  line_index = 0
  for line in f:
    for char_index in range(0, len(line)):
      if line[char_index] == '#':
        lights[line_index][char_index] = 1
    line_index += 1


for attempt in range(0,100):
  lights_tmp = deepcopy(lights)
  #print lights_tmp
  for x in range(0, 100):
    for y in range(0, 100):
      count_on = 0
      if x-1>=0 and y-1>=0:
        count_on +=1 if lights_tmp[x-1][y-1] == 1 else 0
      if y-1>=0:
        count_on +=1 if lights_tmp[x][y-1] == 1 else 0
      if x+1<100 and y-1>=0:
        count_on +=1 if lights_tmp[x+1][y-1] == 1 else 0
      if x-1>=0:
        count_on +=1 if lights_tmp[x-1][y] == 1 else 0
      if x+1<100:
        count_on +=1 if lights_tmp[x+1][y] == 1 else 0
      if x-1>=0 and y+1<100:
        count_on +=1 if lights_tmp[x-1][y+1] == 1 else 0
      if y+1<100:
        count_on +=1 if lights_tmp[x][y+1] == 1 else 0
      if x+1<100 and y+1<100:
        count_on +=1 if lights_tmp[x+1][y+1] == 1 else 0
      #print "Value: ", lights_tmp[x][y]
      #print "Neighbors on for %s, %s: %s" % (x, y, count_on)
      if lights[x][y] == 1:
        if count_on != 2 and count_on != 3:
          if (x==0 and y==0) or (x==0 and y==99) or (x==99 and y==0) or (x==99 and y==99):
            continue
          else:
            lights[x][y] = 0
      else:
        if count_on == 3:
          lights[x][y] = 1
  #print lights

#print lights
count_1 = 0
for i in range(len(lights)):
  for j in range(len(lights[i])):
    count_1 += 1 if lights[i][j] == 1 else 0

print "Count: ", count_1

