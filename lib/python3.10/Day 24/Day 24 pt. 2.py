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

rock_x, rock_y, rock_z, rock_vx, rock_vy, rock_vz = sympy.symbols("rock_x, rock_y, rock_z, rock_vx, rock_vy, rock_vz")

equations = []

i = 0
while i < len(lst):
    hailstone_x = lst[i][0]
    hailstone_y = lst[i][1]
    hailstone_z = lst[i][2]
    hailstone_vx = lst[i][3]
    hailstone_vy = lst[i][4]
    hailstone_vz = lst[i][5]

    equations.append((rock_x - hailstone_x) * (hailstone_vy - rock_vy) - (rock_y - hailstone_y) * (hailstone_vx - rock_vx))
    equations.append((rock_y - hailstone_y) * (hailstone_vz - rock_vz) - (rock_z - hailstone_z) * (hailstone_vy - rock_vy))

    i += 1

answers = sympy.solve(equations)
print(answers)
print(answers[0][rock_x] + answers[0][rock_y] + answers[0][rock_z])
