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
    best_green_cubes = 0
    best_blue_cubes = 0
    best_red_cubes = 0
    while i < len(split_lst[game_num - 1]):
        if num:
            num_cubes = int(split_lst[game_num - 1][i])
            num = False
        else:
            if i + 1 < len(split_lst[game_num - 1]):
                color = split_lst[game_num - 1][i][:-1]
            else:
                color = split_lst[game_num - 1][i]
            if color == "green":
                if num_cubes > best_green_cubes:
                    best_green_cubes = num_cubes
            if color == "blue":
                if num_cubes > best_blue_cubes:
                    best_blue_cubes = num_cubes
            if color == "red":
                if num_cubes > best_red_cubes:
                    best_red_cubes = num_cubes
            num = True
        i += 1
    total += best_red_cubes * best_blue_cubes * best_green_cubes
    game_num +=1
print(total)
