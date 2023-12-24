beams = open('Beams', 'r')
lst = []

for line in beams.readlines():
    word = line.strip()
    temp_list = []
    for char in word:
        temp_list.append(char)
    lst.append(temp_list)

past_beams = []
spots_visited = []
queue = [(0, 0, "down")]
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
print(len(spots_visited))
