almanac = open('Almanac', 'r')
lst = []
total = 0
for line in almanac.readlines():
    word = line.strip()
    lst.append(word)
print(lst)
seed_list = lst[0].split()
seed_list.pop(0)
i = 0
while i < len(seed_list):
    seed_list[i] = int(seed_list[i])
    i += 1
already_mapped = []
for seed in seed_list:
    already_mapped.append(False)
for line in lst:
    if line == '':
        i = 0
        while i < len(already_mapped):
            already_mapped[i] = False
            i += 1
    elif line[0].isdigit():
        split_line = line.split()
        input_end = int(split_line[1]) + int(split_line[2]) - 1
        seed_num = 0
        while seed_num < len(seed_list):
            if already_mapped[seed_num]:
                pass
            elif int(split_line[1]) <= seed_list[seed_num] <= input_end:
                seed_list[seed_num] = seed_list[seed_num] - int(split_line[1]) + int(split_line[0])
                already_mapped[seed_num] = True
            seed_num += 1
lowest_loc = seed_list[0]
for seed in seed_list:
    if seed < lowest_loc:
        lowest_loc = seed
print(lowest_loc)