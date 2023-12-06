races = open('Races', 'r')
lst = []
total = 1
for line in races.readlines():
    word = line.strip()
    lst.append(word)
split_lst = []
for line in lst:
    split_lst.append(line.split())
i = 1
all_possible_wins = []
while i < len(split_lst[0]):
    all_wins_in_trial = 0
    time_pressed = 0
    while time_pressed < int(split_lst[0][i]):
        movement_time = int(split_lst[0][i]) - time_pressed
        distance = time_pressed * movement_time
        if distance > int(split_lst[1][i]):
            all_wins_in_trial += 1
        time_pressed += 1
    all_possible_wins.append(all_wins_in_trial)
    i += 1
for win in all_possible_wins:
    total *= win
print(total)
print(all_possible_wins)