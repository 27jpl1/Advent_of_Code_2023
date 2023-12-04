engine = open('Engine', 'r')
lst = []
total = 0
for line in engine.readlines():
    word = line.strip()
    lst.append(word)
line_num = 0
for line in lst:
    cur_num = ""
    char_num = 0
    symbol_before = False
    symbol_diagonal = False
    for char in line:
        if char == "." or char_num == len(line) - 1:
            if char.isdigit():
                cur_num += char
            if symbol_before:
                if cur_num == "":
                    pass
                else:
                    total += int(cur_num)
                    cur_num = ""
                    symbol_diagonal = False
                    symbol_before = False
            elif line_num == 0:
                if char_num == len(cur_num):
                    for character in lst[line_num + 1][(char_num - len(cur_num)): char_num + 1]:
                        if character != ".":
                            symbol_diagonal = True
                else:
                    for character in lst[line_num + 1][(char_num - len(cur_num) - 1): char_num + 1]:
                        if character != ".":
                            symbol_diagonal = True
            elif line_num == len(lst) - 1:
                if char_num == len(cur_num):
                    for character in lst[line_num - 1][(char_num - len(cur_num)): char_num + 1]:
                        if character != ".":
                            symbol_diagonal = True
                else:
                    for character in lst[line_num - 1][(char_num - len(cur_num) - 1): char_num + 1]:
                        if character != ".":
                            symbol_diagonal = True
            else:
                if char_num == len(cur_num):
                    for character in lst[line_num + 1][(char_num - len(cur_num)): char_num + 1]:
                        if character != ".":
                            symbol_diagonal = True
                    for character in lst[line_num - 1][(char_num - len(cur_num)): char_num + 1]:
                        if character != ".":
                            symbol_diagonal = True
                else:
                    for character in lst[line_num + 1][(char_num - len(cur_num) - 1): char_num + 1]:
                        if character != ".":
                            symbol_diagonal = True
                    for character in lst[line_num - 1][(char_num - len(cur_num) - 1): char_num + 1]:
                        if character != ".":
                            symbol_diagonal = True
            if symbol_diagonal:
                if cur_num != "":
                    total += int(cur_num)
                    cur_num = ""
            else:
                cur_num = ""
            symbol_before = False
            symbol_diagonal = False
        elif char.isdigit():
            cur_num += char
        elif char != ".":
            if cur_num != "":
                total += int(cur_num)
                cur_num = ""
            symbol_before = True
            symbol_diagonal = False
        char_num += 1
    line_num += 1
print(total)