garden = open('Garden', 'r')
lst = []

for line in garden.readlines():
    word = line.strip()
    temp_list = []
    for char in word:
        temp_list.append(char)
    lst.append(temp_list)

i = 0
s = ()
while i < len(lst):
    j = 0
    while j < len(lst[0]):
        if lst[i][j] == "S":
            s = (i,j)
        j += 1
    i += 1

for line in lst:
    for char in line:
        print(char, end="")
    print()

cycles = 0
queue = [s]
while cycles < 64:
    new_queue = []
    spots_visited = []
    while len(queue) > 0:
        spot = queue.pop(0)
        row = spot[0]
        col = spot[1]
        if row - 1 >= 0 and lst[row - 1][col] != "#" and (row - 1, col) not in spots_visited:
            new_queue.append((row - 1, col))
            spots_visited.append((row - 1, col))
        if row + 1 < len(lst) and lst[row + 1][col] != "#" and (row + 1, col) not in spots_visited:
            new_queue.append((row + 1, col))
            spots_visited.append((row + 1, col))
        if col - 1 >= 0 and lst[row][col - 1] != "#" and (row, col - 1) not in spots_visited:
            new_queue.append((row, col - 1))
            spots_visited.append((row, col - 1))
        if col + 1 < len(lst[row]) and lst[row][col + 1] != "#" and (row, col + 1) not in spots_visited:
            new_queue.append((row, col + 1))
            spots_visited.append((row, col + 1))
    queue = new_queue.copy()
    cycles += 1

print(len(new_queue))
