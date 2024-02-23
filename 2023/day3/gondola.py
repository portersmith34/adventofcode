import re

file = open("test values.txt", "r")
linesList= file.readlines()

for line in linesList:
    
    print(line.strip())