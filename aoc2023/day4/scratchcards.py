
def find_winning_cards(linesList, numWin):
    sum = 0
    
    for line in linesList:
        line = line.strip()
        split = line.split(" ")
        while "" in split:
            split.remove("")
        wining_numbers = split[2:numWin+2]
        numbers_you_have = split[numWin+3: len(split)]
        count = 0
        for num in wining_numbers:
            if num in numbers_you_have:
                count += 1
        if count > 0:
            sum += 2**(count-1)
    return(sum)