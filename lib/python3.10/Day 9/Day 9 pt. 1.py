sensor_values = open('Sensor Values', 'r')
lst = []
total = 1
for line in sensor_values.readlines():
    word = line.strip()
    temp_list = []
    for char in word.split():
        temp_list.append(int(char))
    lst.append(temp_list)


def derivate_list(lst) -> list[int]:
    i = 0
    new_lst = []
    while i < len(lst) - 1:
        new_lst.append(lst[i + 1] - lst[i])
        i += 1
    return new_lst


def change (lst) -> int:
    if lst == [0] * len(lst):
        return 0
    else:
        return lst[-1] + change(derivate_list(lst))


print(lst)
total = 0
for set in lst:
    total += change(set)
print(total)
