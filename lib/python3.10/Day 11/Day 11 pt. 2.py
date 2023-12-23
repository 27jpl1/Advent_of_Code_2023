cosmic_space = open('Cosmic Space', 'r')
lst = []
for line in cosmic_space.readlines():
    word = line.strip()
    temp_list = []
    for char in word:
        temp_list.append(char)
    lst.append(temp_list)

blank_rows = []
row = 0
while row < len(lst):
    row_has_octothorpe = False
    col = 0
    while col < len(lst[0]):
        if lst[row][col] == "#":
            row_has_octothorpe = True
            col = len(lst[0])
        col += 1
    if not row_has_octothorpe:
        blank_rows.append(row)
    row += 1

blank_columns = []
col = 0
while col < len(lst[0]):
    col_has_octothorpe = False
    row = 0
    while row < len(lst):
        if lst[row][col] == "#":
            col_has_octothorpe = True
            row = len(lst)
        row += 1
    if not col_has_octothorpe:
        blank_columns.append(col)
    col += 1

octothorpes = []
row = 0
while row < len(lst):
    col = 0
    while col < len(lst[0]):
        if lst[row][col] == "#":
            octothorpes.append((row, col))
        col += 1
    row += 1


def calculate_distance(first, second):
    dist = 0
    expanses = 0
    if first[0] > second[0]:
        for row in blank_rows:
            if first[0] > row > second[0]:
                expanses += 1
    else:
        for row in blank_rows:
            if second[0] > row > first[0]:
                expanses += 1
    if first[1] > second[1]:
        for col in blank_columns:
            if first[1] > col > second[1]:
                expanses += 1
    else:
        for col in blank_columns:
            if second[1] > col > first[1]:
                expanses += 1
    dist += expanses * 999999
    return dist


distance = 0
octothorpe = 0
while octothorpe < len(octothorpes):
    pair = octothorpe + 1
    while pair < len(octothorpes):
        distance += calculate_distance(octothorpes[octothorpe], octothorpes[pair])
        distance += abs(octothorpes[octothorpe][0] - octothorpes[pair][0]) + abs(octothorpes[octothorpe][1] - octothorpes[pair][1])
        pair += 1
    octothorpe += 1

print(distance)
