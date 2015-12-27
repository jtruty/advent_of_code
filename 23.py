instrs = []
with open("23_input.txt") as f:
  instrs = f.readlines()
regs = {'a':0, 'b':0}

current_line = 0
while current_line < len(instrs):
  instr = instrs[current_line].strip().split(" ")
  print instr
  if len(instr) == 3:
    if instr[0] == "jio":
      reg = instr[1][0]
      print reg
      if regs[reg] == 1:
        current_line += int(instr[2])
        continue
    if instr[0] == "jie":
      reg = instr[1][0]
      if regs[reg] % 2 == 0:
        current_line += int(instr[2])
        continue
  if len(instr) == 2:
    if instr[0] == "jmp":
      current_line += int(instr[1])
      continue
    reg = instr[1]
    if instr[0] == "inc":
      regs[reg] += 1
    if instr[0] == "hlf":
      regs[reg] = int(regs[reg]/2)
    if instr[0] == "tpl":
      regs[reg] = regs[reg] * 3
  current_line += 1
  print current_line
  print regs

print regs
