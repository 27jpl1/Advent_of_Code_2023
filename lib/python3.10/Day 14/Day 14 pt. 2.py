reflector_dish = open('Reflector Dish', 'r')
lst = []
total = 0
for line in reflector_dish.readlines():
    word = line.strip()
    temp_list = []
    for char in word:
        temp_list.append(char)
    lst.append(temp_list)


def north():
    row = 1
    while row < len(lst):
        col = 0
        while col < len(lst[0]):
            if lst[row][col] == "O":
                temp_row = row - 1
                while temp_row >= 0:
                    if lst[temp_row][col] == "O" or lst[temp_row][col] == "#":
                        break
                    else:
                        lst[temp_row + 1][col] = "."
                        lst[temp_row][col] = "O"
                    temp_row -= 1
            col += 1
        row += 1


def west():
    row = 0
    while row < len(lst):
        col = 1
        while col < len(lst[0]):
            if lst[row][col] == "O":
                temp_col = col - 1
                while temp_col >= 0:
                    if lst[row][temp_col] == "O" or lst[row][temp_col] == "#":
                        break
                    else:
                        lst[row][temp_col + 1] = "."
                        lst[row][temp_col] = "O"
                    temp_col -= 1
            col += 1
        row += 1


def south():
    row = len(lst) - 1
    while row >= 0:
        col = 0
        while col < len(lst):
            if lst[row][col] == "O":
                temp_row = row + 1
                while temp_row < len(lst[0]):
                    if lst[temp_row][col] == "O" or lst[temp_row][col] == "#":
                        break
                    else:
                        lst[temp_row - 1][col] = "."
                        lst[temp_row][col] = "O"
                    temp_row += 1
            col += 1
        row -= 1


def east():
    row = 0
    while row < len(lst):
        col = len(lst[0]) - 1
        while col >= 0:
            if lst[row][col] == "O":
                temp_col = col + 1
                while temp_col < len(lst[0]):
                    if lst[row][temp_col] == "O" or lst[row][temp_col] == "#":
                        break
                    else:
                        lst[row][temp_col - 1] = "."
                        lst[row][temp_col] = "O"
                    temp_col += 1
            col -= 1
        row += 1


cycles = 1000
j = 1
# Cycle 1000 has the same value as cycle 1,000,000,000 (1 billion)
while j <= cycles:
    north()
    west()
    south()
    east()
    j += 1

i = 0
while i < len(lst):
    for rock in lst[i]:
        if rock == "O":
            total += len(lst) - i
    i += 1
print(total)