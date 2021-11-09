import os

opts = {
  "0": "Connect A to data bus",
  "1": "Write data bus to A",
  "2": "Connect B to data bus",
  "3": "Write data bus to B",
  "4": "Connect A+B to data bus",
  "5": "Connect A-B to data bus",
  "6": "Connect B-A to data bus",
  "7": "Connect memory to data bus",
  "8": "Write data bus to memory",
  "9": "Connect PC to data bus",
  "a": "Write data bus to PC",
  "b": "Connect operand to data bus",
  "c": "Connect operand to address bus",
  "d": "Connect A to address bus",
  "e": "Connect B to address bus",
  "f": "Update ALU inputs",
}

current_opts = []

while True:
  os.system("clear")
  for k, v in opts.items():
    print("[*]" if k in current_opts else "[ ]", k + ": " + v)

  currentbin = 0

  for opt in current_opts:
    currentbin |= (1 << int(opt, 16))

  print("x: clear")
  print()
  print("Bin:", bin(currentbin)[2:].zfill(16))
  print("Hex:", hex(currentbin)[2:].zfill(4))

  newopt = input("> ")
  if not newopt:
    continue
  if newopt == "x":
    current_opts = []
    continue

  if newopt in current_opts:
    current_opts.remove(newopt)
  else:
    current_opts.append(newopt)
