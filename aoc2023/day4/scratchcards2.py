import copy

def duplicate(curr_index, card_list, duplication_number, max):
    for i in range(1,duplication_number+1):
        card_to_copy = card_list[curr_index].card_number-1 + i
        if card_to_copy < max:
            newCard = copy.deepcopy(card_list[card_to_copy])
            card_list.append(newCard)

def find_all_cards(lines_List, numWin):
    print("num lines:",len(lines_List))
    card_list = []
    card_num = 0
    # create all cards
    for line in lines_List:
        card_num += 1
        line = line.strip()
        split = line.split(" ")
        while "" in split:
            split.remove("")
        card_list.append(Card(card_num, split[2:numWin+2], split[numWin+3: len(split)]))

    i = 0
    while i < len(card_list):
        count = 0
        # only find count the 1st time
        if card_list[i].count is False:
            for num in card_list[i].winning_numbers:
                if num in card_list[i].numbers_you_have:
                    count += 1
            card_list[i].count = count
        else:
            count = card_list[i].count
        if count > 0:   
            duplicate(i, card_list, count, len(lines_List))
        i += 1
    return(len(card_list))

class Card:
    count = False
    
    def __init__(self, card_number, winning_numbers, numbers_you_have):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.numbers_you_have = numbers_you_have


