mirrors = open('Mirrors', 'r')
lst = []
temp_list = []
for line in mirrors.readlines():
    word = line.strip()
    if word == "":
        lst.append(temp_list)
        temp_list = []
    else:
        temp_list.append(word)
lst.append(temp_list)

total = 0
i = 0
while i < len(lst):
    point_of_incidence = None
    row = 1
    has_row_incidence = False
    while row < len(lst[i]):
        lst[i].insert(row, "." * len(lst[i][0]))
        is_point_of_incidence = True
        rows_away = 1
        while row - rows_away >= 0 and row + rows_away < len(lst[i]):
            if lst[i][row - rows_away] != lst[i][row + rows_away]:
                is_point_of_incidence = False
                rows_away = len(lst[i])
            rows_away += 1
        lst[i].pop(row)
        if is_point_of_incidence:
            has_row_incidence = True
            point_of_incidence = row
            total += point_of_incidence * 100
            row = len(lst[i])
        row += 1
    if not has_row_incidence:
        col = 1
        while col < len(lst[i][0]):
            row = 0
            while row < len(lst[i]):
                lst[i][row] = lst[i][row][0:col] + "." + lst[i][row][col:]
                row += 1
            has_column_incidence = True
            columns_away = 1
            while col - columns_away >= 0 and col + columns_away < (len(lst[i][0])):
                row = 0
                while row < len(lst[i]):
                    if lst[i][row][col - columns_away] != lst[i][row][col + columns_away]:
                        has_column_incidence = False
                    row += 1
                columns_away += 1

            row = 0
            while row < len(lst[i]):
                lst[i][row] = lst[i][row][0:col] + lst[i][row][col + 1:]
                row += 1

            if has_column_incidence:
                total += col
                col = len(lst[i][0])
            col += 1
    i += 1


print(lst)
print(total)