import re
numRed = 12
numGreen = 13
numBlue = 14
count = 0
numPattern = r"[0-9]+"

file = open("cubegame input.txt", "r")
linesList= file.readlines()

for line in linesList:
  clear = True
  split = line.split(":")
  id = re.search(numPattern, split[0]).group()
  sets = split[1].split(";")
  for set in sets:
    red = re.findall(r"[0-9]+\sred", set)
    green = re.findall(r"[0-9]+\sgreen", set)
    blue = re.findall(r"[0-9]+\sblue", set)
    if (len(red) > 0 and int(re.findall(numPattern, red[0])[0]) > numRed):
      clear = False
      break
    if (len(green) > 0 and int(re.findall(numPattern, green[0])[0]) > numGreen):
      clear = False
      break
    if (len(blue) > 0 and int(re.findall(numPattern, blue[0])[0]) > numBlue):
      clear = False
      break
  if (clear):
    count += int(id)
print(count)
