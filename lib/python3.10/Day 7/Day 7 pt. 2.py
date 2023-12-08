# Possibly could do this by adding 1 to every count after created the dict for the num of jokers.
# Would have to be careful with pairs/possible full houses.
# A full house would be two sets of three cards otherwise it would be four of a kind
# It is not possible to have two pair with a joker
# Still possible to have no pairs
def get_value(hand) -> float | int:
    card_dict = {}
    set_of_3 = False
    set_of_2 = False
    joker_count = 0
    for card in hand:
        if card == "J":
            joker_count += 1
        elif card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    if joker_count > 0:
        if joker_count == 5:
            return 5
        highest_card = ("", 0)
        for card in card_dict:
            if int(card_dict[card]) > highest_card[1]:
                highest_card = (card, card_dict[card])
        card_dict[highest_card[0]] += joker_count
    if len(card_dict) == 2:
        for card in card_dict:
            if card_dict[card] == 3:
                set_of_3 = True
            elif card_dict[card] == 2:
                set_of_2 = True
        if set_of_2 and set_of_3:
            return 3.5
    for card in card_dict:
        if card_dict[card] == 5:
            return 5
        elif card_dict[card] == 4:
            return 4
        elif card_dict[card] == 3:
            return 3
        elif card_dict[card] == 2:
            if not set_of_2:
                set_of_2 = True
            else:
                return 2.5
    if set_of_2:
        return 2
    else:
        return 1

def tiebreaker(hand1, hand2) -> str:
    i = 0
    value_dict = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9" : 9, "T": 10, "Q": 12, "K": 13, "A": 14}
    while i < len(hand1):
        if hand1[i] == hand2[i]:
            pass
        else:
            if value_dict[hand1[i]] == value_dict[hand2[i]]:
                pass
            elif value_dict[hand1[i]] > value_dict[hand2[i]]:
                return hand1
            else:
                return hand2
        i += 1


cards = open('Camel_Cards', 'r')
lst = []
total = 0
for line in cards.readlines():
    word = line.strip()
    lst.append(word)
split_list = []
for set in lst:
    split_list.append(set.split())
card_to_number_dict = {}
for set in split_list:
    card_to_number_dict[set[0]] = set[1]
sorted_cards = [split_list[0][0]]
i = 1
while i < len(split_list):
    hand = split_list[i][0]
    print(hand, get_value(hand))
    for sorted_card in sorted_cards:
        if get_value(sorted_card) > get_value(hand):
            pass
        elif get_value(sorted_card) == get_value(hand):
            index = sorted_cards.index(sorted_card)
            if hand == tiebreaker(hand, sorted_card):
                sorted_cards.insert(index, hand)
                break
            else:
                pass
        else:
            index = sorted_cards.index(sorted_card)
            sorted_cards.insert(index, hand)
            break
    if hand not in sorted_cards:
        sorted_cards.append(hand)
    i += 1
print(sorted_cards)
rank = 1
while len(sorted_cards) > 0:
    total += int(card_to_number_dict[sorted_cards.pop()]) * rank
    rank += 1
print(total)