import re

def part1():
  total = 0
  with open('8_input.txt', 'r') as f:
    for line in f:
      total_string = line.strip()
      adj_string = total_string[1:-1] #strip leading and ending quotes
      adj_string = re.sub(r'\\\\', "x", adj_string)
      adj_string = re.sub(r'\\\"', "x", adj_string)
      adj_string = re.sub(r'\\x\w\w', "x", adj_string)
      num_chars_in_memory = len(total_string) - len(adj_string)
      total += num_chars_in_memory

  print total

def part2():
  total = 0
  with open('8_input.txt', 'r') as f:
    for line in f:
      total_string = line.strip()
      adj_string = total_string[1:-1] #strip leading and ending quotes
      adj_string = re.sub(r'\\', "xx", adj_string)
      adj_string = re.sub(r'\"', "xx", adj_string)
      num_chars_in_memory = len(adj_string) + 6 - len(total_string)
      total += num_chars_in_memory
  print total

part2()

