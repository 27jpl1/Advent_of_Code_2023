card_file = open('Cards', 'r')
lst = []
total = 0
for line in card_file.readlines():
    word = line.strip()
    lst.append(word)
cards = []
for card in lst:
    cards.append(card.split())
for card in cards:
    winning_numbers = []
    points = 0
    add_to_winnings = True
    for part in card:
        if part.isdigit():
            if add_to_winnings:
                winning_numbers.append(part)
            else:
                if part in winning_numbers:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2
        elif part == "|":
            add_to_winnings = False
    total += points
print(total)
