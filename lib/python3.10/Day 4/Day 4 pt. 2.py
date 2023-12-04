card_file = open('Cards', 'r')
lst = []
total = 0
for line in card_file.readlines():
    word = line.strip()
    lst.append(word)
cards = []
for card in lst:
    cards.append(card.split())
i = 0
card_counts = {}
while i < len(lst):
    card_counts[i + 1] = 1
    i += 1
card_num = 1
for card in cards:
    count = 0
    winning_numbers = []
    add_to_winnings = True
    for part in card:
        if part.isdigit():
            if add_to_winnings:
                winning_numbers.append(part)
            else:
                if part in winning_numbers:
                    count += 1
        elif part == "|":
            add_to_winnings = False
    while count > 0:
        card_counts[card_num + count] += card_counts[card_num]
        count -= 1
    card_num += 1
for count in card_counts:
    total += card_counts[count]
print(total)