from queue import Queue

def find_all_cards(linesList, numWin):
    sum = 0
    card_queue = Queue()
    count_list = {}
    card_number = 0
    for line in linesList:
        card_number += 1
        line = line.strip()
        split = line.split(" ")
        while "" in split:
            split.remove("")
        winning_numbers = split[2:numWin+2]
        numbers_you_have = split[numWin+3: len(split)]
        
        count = 0
        for num in winning_numbers:
            if num in numbers_you_have:
                count += 1
        
        count_list[card_number] = count
        card_queue.put(card_number)
    
    while not card_queue.empty():
        curr_card = card_queue.get()
        for i in range(curr_card + 1, count_list[curr_card] + curr_card + 1):
            card_queue.put(i)
        sum +=1
    return(sum)