hail_stones = open('Hail Stones', 'r')
lst = []
for line in hail_stones.readlines():
    word = line.strip()
    temp_word = ""
    temp_list = []
    for char in word:
        if char.isdigit() or char == "-":
            temp_word += char
        elif temp_word != "":
            temp_list.append(int(temp_word))
            temp_word = ""
    temp_list.append(int(temp_word))
    lst.append(temp_list)

total = 0
i = 0
while i < len(lst):
    a1 = lst[i][4]
    b1 = -lst[i][3]
    c1 = lst[i][4] * lst[i][0] - lst[i][3] * lst[i][1]
    j = i + 1
    while j < len(lst):
        a2 = lst[j][4]
        b2 = -lst[j][3]
        c2 = lst[j][4] * lst[j][0] - lst[j][3] * lst[j][1]
        if a1 * b2 == b1 * a2:
            pass
        else:
            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                if (x - lst[i][0]) * lst[i][3] >= 0 and (y - lst[i][1]) * lst[i][4] >= 0 and (x - lst[j][0]) * lst[j][3] >= 0 and (y - lst[j][1]) * lst[j][4] >= 0:
                    total += 1
        j += 1
    i += 1
print(total)
