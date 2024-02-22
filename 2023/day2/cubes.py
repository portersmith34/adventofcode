numRed = 12
numGreen = 13
numBlue = 14

file = open("cubegame input.txt", "r")
linesList= file.readlines()

for line in linesList[:10]:
  print(line)