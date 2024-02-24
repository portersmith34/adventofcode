import re

def add_to_dict(key, val, dict):
  if key in dict.keys():
    dict[key].append(val)
  else:
    dict[key] = [val,]

def find_gear_ratio(linesList):
  numPattern = r"[\d]+"
  symPattern = r"[*]"
  prevLine = []
  prevNums = []
  prevSyms = []
  ratios = {}
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
        if prevNums[j][0] == currSyms[i][0]-1 or prevNums[j][0] == currSyms[i][0] or prevNums[j][0] == currSyms[i][0]+1 \
            or prevNums[j][1]-1 == currSyms[i][0]-1 or prevNums[j][1]-1 == currSyms[i][0] or prevNums[j][1]-1 == currSyms[i][0]+1: 
          add_to_dict(currSyms[i][0], prevLine[j], ratios)
    
    # if prev symbol matches up with curr number
    for i in range(len(prevSyms)):
      for j in range(len(currNums)):
        if currNums[j][0] == prevSyms[i][0]-1 or currNums[j][0] == prevSyms[i][0] or currNums[j][0] == prevSyms[i][0]+1 \
            or currNums[j][1]-1 == prevSyms[i][0]-1 or currNums[j][1]-1 == prevSyms[i][0] or currNums[j][1]-1 == prevSyms[i][0]+1: 
          add_to_dict(prevSyms[i][0], nums[j], ratios)
    
    # check curr line 
    for i in range(len(currSyms)):
      for j in range(len(currNums)):
        if currNums[j][0] == currSyms[i][1] or currNums[j][1] == currSyms[i][0]: 
          add_to_dict(currSyms[i][0], nums[j], ratios)
    
    for sym in prevSyms:
      if sym[0] in ratios.keys():
        if len(ratios[sym[0]]) == 2:
          print("doing the math")
          sum += int(ratios[sym[0]][0]) * int(ratios[sym[0]][1])
        del ratios[sym[0]]
        
    prevLine = nums
    prevNums = currNums
    prevSyms = currSyms
  return(sum)

