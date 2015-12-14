import re

start = "3113322113"
for i in range(40):
  result = ""
  start_idx = 0
  while start_idx<len(start):
    count = 1
    key = start[start_idx]
    scan_idx = start_idx + 1
    while scan_idx<len(start) and start[start_idx] == start[scan_idx]:
      count += 1
      scan_idx += 1
    result += str(count) + key
    start_idx += count
  start = result
print result, len(result)
