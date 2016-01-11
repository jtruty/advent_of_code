from itertools import permutations

with open("9_input.txt") as f:
    routes = f.readlines()

route_mat, perms, count = [[0 for i in range(8)] for i in range(8)], [''.join(p) for p in permutations('01234567')], 0

for i in range(8):
    for j in range(i+1, 8):
        route_mat[i][j] = int(routes[count].split(' ')[4])
        route_mat[j][i] = int(routes[count].split(' ')[4])
        print count, i, j
        count += 1

short_ans = 9999
long_ans = 0
for perm in perms:
    temp = 0
    for j in range(len(perm)-1):
        temp += route_mat[int(perm[j])][int(perm[j+1])]
    if(temp < short_ans):
        short_ans = temp
    if(temp > long_ans):
        long_ans = temp
print "Shortest distance: ", short_ans
print "Longest distance: ", long_ans
