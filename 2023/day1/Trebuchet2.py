import re 

def intFromString(num):
  match num:
    case '':
      return ''
    case "one":
      return 1
    case "two":
      return 2
    case "three":
      return 3
    case "four":
      return 4
    case "five":
      return 5
    case "six":
      return 6
    case "seven":
      return 7
    case "eight":
      return 8
    case "nine":
      return 9
    case _:
      return ''
    
def reverse(last):
  temp = ""
  for i in range(len(last)):
    temp += last[len(last)-i-1]
  return temp

sum = 0
file = open("calibration values.txt", "r")
linesList= file.readlines()

for line in linesList:
  line = line.strip()
  blocks = re.split("[1-9]", line)
  nums = re.sub("[a-z]", "", line)
  first = blocks[0]
  last = blocks[len(blocks)-1]
  last = reverse(last)
  search = "one|two|three|four|five|six|seven|eight|nine"
  search1 = re.findall(search, first)
  search = reverse(search)
  search2 = re.findall(search, last)
  if (len(search1) > 0):
   first = intFromString(search1[0])
  else:
    first = ""
  if (len(search2) > 0):
   temp = reverse(search2[0])
   last = intFromString(temp)
  else: 
    last = ""

  if (first == ''):
    first = nums[0]
  if (last == ''):
    last = nums[len(nums)-1]
  val = str(first) + str(last)
  sum += int(val)
print(sum)
