import re 

sum = 0
file = open("calibration values.txt", "r")

for line in file:
  temp = re.sub("[a-z\\n]", "", line)
  val = temp[0]+ temp[len(temp)-1]
  sum += int(val)
print("sum: "+str(sum))