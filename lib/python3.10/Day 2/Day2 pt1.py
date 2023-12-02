games = open('games', 'r')
lst = []
game_num = 1
total = 0
for line in games.readlines():
    word = line.strip()
    lst.append(word)
split_lst = []
for line in lst:
    split_lst.append(line.split())
while game_num < len(lst) + 1:
    i = 2
    num = True
    game_works = True
    color = ""
    while i < len(split_lst[game_num - 1]):
        if num:
            num_cubes = int(split_lst[game_num - 1][i])
            num = False
        else:
            if i + 1 < len(split_lst[game_num - 1]):
                color = split_lst[game_num - 1][i][:-1]
            else:
                color = split_lst[game_num - 1][i]
            print(color)
            if color == "green":
                if num_cubes > 13:
                    game_works = False
            if color == "blue":
                if num_cubes > 14:
                    game_works = False
            if color == "red":
                if num_cubes > 12:
                    game_works = False
            num = True
        i += 1
    if game_works:
        total += game_num
    game_num +=1
print(total)
