import sys

almanac = open('Almanac', 'r')
lst = []
total = 0
for line in almanac.readlines():
    word = line.strip()
    lst.append(word)
print(lst)
seed_ranges = lst[0].split()
seed_ranges.pop(0)
seed_range = 0
lowest_loc = sys.maxsize
while seed_range < len(seed_ranges): # probably need to integrate this into the function because i cannot make a list of all the seeds without losing memory
    seed_list = []
    already_mapped = []
    j = int(seed_ranges[seed_range])
    while j < int(seed_ranges[seed_range]) + int(seed_ranges[seed_range + 1]):
        seed_list.append(j)
        j += 1
    print("seed_list done")
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
                elif int(split_line[1]) <= seed_list[seed_num] <= input_end: ### Here could probably break if > input_end because the seeds are in numerical order
                    seed_list[seed_num] = seed_list[seed_num] - int(split_line[1]) + int(split_line[0])
                    already_mapped[seed_num] = True
                seed_num += 1
        print("one set of calculations is done")
    for seed in seed_list:
        if seed < lowest_loc:
            lowest_loc = seed
    seed_range += 2
    print("current lowest_loc", lowest_loc)
print(lowest_loc)