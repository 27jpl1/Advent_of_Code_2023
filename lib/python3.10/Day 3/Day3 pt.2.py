# takes in the line_num and char_num of final digit plus the len of the cur_num and check the neighbors for *s
# this needs to be updated/pushed into main stuff because need to check when it is on the side and adjust accordingly
# could add an artifical ring of dots to make to whole things easier...
def check_neighbor(line_num: int, char_num: int, cur_num_len: int) -> (int, int):
    star_spots = []
    start_point = (line_num - 1, char_num - cur_num_len - 1)
    cycles = 3
    spots_to_look_over = cur_num_len + 2
    i = 0
    while i < cycles:
        spots_looked_over = 0
        while spots_looked_over < spots_to_look_over:
            if lst[start_point[0] + i][start_point[1] + spots_looked_over] == "*":
                star_spots.append((start_point[0] + i, start_point[1] + spots_looked_over))
            spots_looked_over += 1
        i += 1
    return star_spots


engine = open('Engine', 'r')
lst = []
total = 0
line_len = 0
for line in engine.readlines():
    word = line.strip()
    line_len = len(word)
    lst.append("." + word + ".")
period_line = "." * (line_len + 2)
lst.insert(0, period_line)
lst.append(period_line)
line_num = 0
stars = {}
for line in lst:
    char_num = 0
    for char in line:
        if char == "*":
            stars[(line_num, char_num)] = []
        char_num += 1
    line_num += 1
print(stars)
line_num = 0
for line in lst:
    char_num = 0
    cur_num = ""
    for char in line:
        if char.isdigit():
            cur_num += char
        else:
            if cur_num != "":
                star_spots = check_neighbor(line_num, char_num, len(cur_num))
                for spot in star_spots:
                    stars[spot].append(cur_num)
            cur_num = ""
        char_num += 1
    line_num += 1
print(stars)
for star in stars:
    if len(stars[star]) == 2:
        total += int(stars[star][0]) * int(stars[star][1])
print(total)