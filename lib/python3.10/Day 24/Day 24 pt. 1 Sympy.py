import sympy

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
    j = i + 1
    sx1 = lst[i][0]
    sy1 = lst[i][1]
    vx1 = lst[i][3]
    vy1 = lst[i][4]
    while j < len(lst):
        sx2 = lst[j][0]
        sy2 = lst[j][1]
        vx2 = lst[j][3]
        vy2 = lst[j][4]

        px, py = sympy.sympify("px, py")
        answers = sympy.solve([vy1 * (px - sx1) - vx1 * (py - sy1), vy2 * (px - sx2) - vx2 * (py - sy2)])
        if not answers:
            pass
        else:
            x = answers[px]
            y = answers[py]
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                if (x - sx1) * vx1 >= 0 and (x - sx2) * vx2 >= 0 and (y - sy1) * vy1 >= 0 and (y - sy2) * vy2 >= 0:
                    total += 1
        j += 1
    i += 1

print(total)
