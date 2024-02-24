import re

def find_part_numbers(linesList):
  numPattern = r"[\d]+"
  symPattern = r"[*+$#%&@=/-]"
  prevLine = []
  prevNums = []
  prevSyms = []
  sum = 0
  
  for line in linesList:
    currNums = []
    nums = re.findall(numPattern, line)
    for num in nums:
      currNums.append(re.search(num, line).span())
      line = line.replace(str(num), "."*len(num), 1)


    currSyms = []
    syms = re.findall(symPattern, line)
    for sym in syms:
      currSyms.append(re.search("\\"+sym, line).span())
      line = line.replace(str(sym), ".", 1)

    # if prev number matches up with current symbol
    for i in range(len(currSyms)):
      for j in range(len(prevNums)):
        if prevNums[j][0] == currSyms[i][0]-1 or prevNums[j][0] == currSyms[i][0] or prevNums[j][0] == currSyms[i][0]+1: 
          sum += int(prevLine[j])
          prevLine[j] = 0
        elif prevNums[j][1]-1 == currSyms[i][0]-1 or prevNums[j][1]-1 == currSyms[i][0] or prevNums[j][1]-1 == currSyms[i][0]+1: 
          sum += int(prevLine[j])
          prevLine[j] = 0

    # if prev symbol matches up with curr number
    for i in range(len(prevSyms)):
      for j in range(len(currNums)):
        if currNums[j][0] == prevSyms[i][0]-1 or currNums[j][0] == prevSyms[i][0] or currNums[j][0] == prevSyms[i][0]+1: 
          sum += int(nums[j])
          nums[j] = 0
        elif currNums[j][1]-1 == prevSyms[i][0]-1 or currNums[j][1]-1 == prevSyms[i][0] or currNums[j][1]-1 == prevSyms[i][0]+1: 
          sum += int(nums[j])
          nums[j] = 0

    # check curr line 
    for i in range(len(currSyms)):
      for j in range(len(currNums)):
        if currNums[j][0] == currSyms[i][1] or currNums[j][1] == currSyms[i][0]: 
          sum += int(nums[j])
          nums[j] = 0

    prevLine = nums
    prevNums = currNums
    prevSyms = currSyms
  return(sum)