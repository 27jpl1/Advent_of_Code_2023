pipes = open('Pipes', 'r')
lst = []

for line in pipes.readlines():
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

pipes_visited = []
queue = [s]

while len(queue) > 0:
    current_pipe = queue.pop(0)
    row = current_pipe[0]
    col = current_pipe[1]
    if row > 0 and lst[row][col] in "|LJS" and lst[row - 1][col] in "|7F" and (row - 1, col) not in pipes_visited:
        pipes_visited.append((row, col))
        queue.append((row - 1, col))
    if row < len(lst) and lst[row][col] in "|7FS" and lst[row + 1][col] in "|LJ" and (row + 1, col) not in pipes_visited:
        pipes_visited.append((row, col))
        queue.append((row + 1, col))
    if col < len(lst[0]) and lst[row][col] in "-LFS" and lst[row][col + 1] in "-J7" and (row, col + 1) not in pipes_visited:
        pipes_visited.append((row, col))
        queue.append((row, col + 1))
    if col > 0 and lst[row][col] in "-J7S" and lst[row][col - 1] in "-LF" and (row, col - 1) not in pipes_visited:
        pipes_visited.append((row, col))
        queue.append((row, col - 1))
    pipes_visited.append((row, col))

lst[s[0]][s[1]] = "|"

row = 0
while row < len(lst):
    col = 0
    while col < len(lst[0]):
        if (row, col) not in pipes_visited:
            lst[row][col] = "."
        col += 1
    row += 1


def check_right(row, col):
    if (row, col) in pipes_visited:
        return 0
    else:
        col += 1
        crossings = 0
        while col < len(lst[0]):
            if lst[row][col] in "|JL":
                crossings += 1
            col += 1
        return crossings


total_inside = 0
row = 0
while row < len(lst):
    col = 0
    while col < len(lst[0]):
        if check_right(row, col) % 2 == 1:
            total_inside += 1
        col += 1
    row += 1

print(total_inside)