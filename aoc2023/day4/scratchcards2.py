
def find_winning_cards(linesList, numWin):
    total_cards = 0
    
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
            total_cards += 1
            pass
    return(total_cards)