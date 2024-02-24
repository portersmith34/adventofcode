import re
numPattern = r"[0-9]+"

# if num exists then return it
def getNum(color):
  if len(color) > 0:
    return int(re.findall(numPattern, color[0])[0])
  else:
    return 1

file = open("cubegame input.txt", "r")
linesList= file.readlines()
power = 0

for line in linesList:
  numRed = 1
  numGreen = 1
  numBlue = 1
  split = line.split(":")
  sets = split[1].split(";")

  for set in sets:
    # find the number and color
    red = getNum(re.findall(r"[0-9]+\sred", set))
    green = getNum(re.findall(r"[0-9]+\sgreen", set))
    blue = getNum(re.findall(r"[0-9]+\sblue", set))
    # find the max for each color
    if red > numRed:
      numRed = red
    if green > numGreen:
      numGreen = green
    if blue > numBlue:
      numBlue = blue
  power += numRed * numGreen * numBlue
print("total Power:", power)