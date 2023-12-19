reflector_dish = open('Reflector Dish', 'r')
lst = []
total = 0
for line in reflector_dish.readlines():
    word = line.strip()
    temp_list = []
    for char in word:
        temp_list.append(char)
    lst.append(temp_list)
print(lst)
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
i = 0
while i < len(lst):
    for rock in lst[i]:
        if rock == "O":
            total += len(lst) - i
    i += 1
print(total)