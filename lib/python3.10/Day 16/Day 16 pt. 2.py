beams = open('Beams', 'r')
lst = []

for line in beams.readlines():
    word = line.strip()
    temp_list = []
    for char in word:
        temp_list.append(char)
    lst.append(temp_list)

lst.insert(0, ["."] * len(lst[0]))
lst.append(["."] * len(lst[0]))
for line in lst:
    line.insert(0, ".")
    line.append(".")

added_spots = []

col = 0
while col < len(lst[0]):
    added_spots.append((0, col))
    added_spots.append((len(lst) - 1, col))
    col += 1

row = 0
while row < len(lst):
    added_spots.append((row, 0))
    added_spots.append((row, len(lst[0]) - 1))
    row += 1


def check_starting_point(starting_point):
    past_beams = []
    spots_visited = []
    queue = [starting_point]

    while len(queue) > 0:
        current_beam = queue.pop(0)
        row = current_beam[0]
        col = current_beam[1]
        if current_beam[2] == "right":
            if col + 1 < len(lst) and (row, col, "right") not in past_beams:
                past_beams.append((row, col, "right"))
                if lst[row][col + 1] == "|":
                    queue.append((row, col + 1, "up"))
                    queue.append((row, col + 1, "down"))
                elif lst[row][col + 1] == "\\":
                    queue.append((row, col + 1, "down"))
                elif lst[row][col + 1] == "/":
                    queue.append((row, col + 1, "up"))
                else:
                    queue.append((row, col + 1, "right"))
            if (row, col) not in spots_visited:
                spots_visited.append((row, col))
        elif current_beam[2] == "left":
            if col - 1 >= 0 and (row, col, "left") not in past_beams:
                past_beams.append((row, col, "left"))
                if lst[row][col - 1] == "|":
                    queue.append((row, col - 1, "up"))
                    queue.append((row, col - 1, "down"))
                elif lst[row][col - 1] == "\\":
                    queue.append((row, col - 1, "up"))
                elif lst[row][col - 1] == "/":
                    queue.append((row, col - 1, "down"))
                else:
                    queue.append((row, col - 1, "left"))
            if (row, col) not in spots_visited:
                spots_visited.append((row, col))
        elif current_beam[2] == "up":
            if row - 1 >= 0 and (row, col, "up") not in past_beams:
                past_beams.append((row, col, "up"))
                if lst[row - 1][col] == "-":
                    queue.append((row - 1, col, "left"))
                    queue.append((row - 1, col, "right"))
                elif lst[row - 1][col] == "/":
                    queue.append((row - 1, col, "right"))
                elif lst[row - 1][col] == "\\":
                    queue.append((row - 1, col, "left"))
                else:
                    queue.append((row - 1, col, "up"))
            if (row, col) not in spots_visited:
                spots_visited.append((row, col))
        elif current_beam[2] == "down":
            if row + 1 < len(lst[row]) and (row, col, "down") not in past_beams:
                past_beams.append((row, col, "down"))
                if lst[row + 1][col] == "-":
                    queue.append((row + 1, col, "left"))
                    queue.append((row + 1, col, "right"))
                elif lst[row + 1][col] == "/":
                    queue.append((row + 1, col, "left"))
                elif lst[row + 1][col] == "\\":
                    queue.append((row + 1, col, "right"))
                else:
                    queue.append((row + 1, col, "down"))
            if (row, col) not in spots_visited:
                spots_visited.append((row, col))

    for spot in spots_visited:
        if spot in added_spots:
            spots_visited.remove(spot)

    return len(spots_visited)


max_spots_visited = 0
col = 0
while col < len(lst[0]):
    down_visited = check_starting_point((0, col, "down"))
    up_visited = check_starting_point((len(lst[0]) - 1, col, "up"))
    if down_visited > max_spots_visited:
        max_spots_visited = down_visited
    if up_visited > max_spots_visited:
        max_spots_visited = up_visited
    col += 1

row = 0
while row < len(lst):
    right_visited = check_starting_point((row, 0, "right"))
    left_visited = check_starting_point((row, len(lst[0]) - 1, "up"))
    if right_visited > max_spots_visited:
        max_spots_visited = right_visited
    if left_visited > max_spots_visited:
        max_spots_visited = left_visited
    row += 1

print(max_spots_visited - 2)
