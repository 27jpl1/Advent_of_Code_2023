cosmic_space = open('Cosmic Space', 'r')
lst = []
for line in cosmic_space.readlines():
    word = line.strip()
    temp_list = []
    for char in word:
        temp_list.append(char)
    lst.append(temp_list)

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
        lst.insert(row + 1, ["."]*len(lst[0]))
        row += 1
    row += 1

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
        row = 0
        while row < len(lst):
            lst[row].insert(col + 1, ".")
            row += 1
        col += 1
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

distance = 0
octothorpe = 0
while octothorpe < len(octothorpes):
    pair = octothorpe + 1
    while pair < len(octothorpes):
        distance += abs(octothorpes[octothorpe][0] - octothorpes[pair][0]) + abs(octothorpes[octothorpe][1] - octothorpes[pair][1])
        pair += 1
    octothorpe += 1

print(distance)