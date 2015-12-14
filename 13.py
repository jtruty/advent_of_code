from re import findall
from itertools import permutations

m = {}
ppl = set()

with open("13_input.txt") as f:
  for line in f:
      a, s, n, b = findall(r'(\w+) \w+ (\w+) (\d+) .* (\w+)\.', line)[0]
      m[a+b] = int(n) * (1 if s == 'gain' else -1)
      ppl.add(a)

def c(p):
    L = len(p)
    t = 0
    for i in range(L):
        t += m[p[i]+p[i-1]]
        t += m[p[i]+p[(i+1) % L]]
    return t

print(max([c(p) for p in permutations(ppl)]))
