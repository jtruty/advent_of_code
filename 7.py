f = open("7_input.txt")
a = f.readlines()
d = {}
t = {}

for x in a:
    x = x.split("->")
    k = x[1].strip()
    o = x[0].strip().split(" ")
    d[k] = o

def andop(x,y):
    return x & y

def orop(x,y):
    return x | y

def notop(x):
    return ~x

def shift(x, i, d):
    if d == "L":
        return x << i
    else:
        return x >> i

def lookup(x):
    if x.isdigit():
        return int(x)
    if x in t:
        return t[x]
    o = d[x]
    print(o)
    if len(o) == 1:
        if o[0].isdigit():
            t[x] = o[0]
        else:
            t[x] = lookup(o[0])
        return t[x]
    if len(o) == 2:
        t[x] = notop(lookup(o[1]))
        return t[x]
    if len(o) == 3:
        f = lookup(o[0])
        op = o[1]
        s = lookup(o[2])
        if op == "AND":
            t[x] = andop(int(f), s)
        if op == "OR":
            t[x] = orop(int(f), s)
        if op[1:] == "SHIFT":
            t[x] = shift(int(f), int(s), op[0])
        return t[x]

x = "a"
print(lookup(x))
