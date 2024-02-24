
def find_winning_cards(linesList, numWin):
    sum = 0
    
    for line in linesList:
        line = line.strip()
        split = line.split(" ")
        while "" in split:
            split.remove("")
        wining_numbers = split[2:numWin+2]
        numbers_you_have = split[numWin+3: len(split)]
        point_value = 0
        count = 0
        numbers_you_have.sort()
        for num in wining_numbers:
            if num in numbers_you_have:
                count += 1
        if count > 0:
            sum += 2**(count-1)
    return(sum)