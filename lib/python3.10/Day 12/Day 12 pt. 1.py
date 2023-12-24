springs = open('Springs', 'r')

lst = []
for line in springs.readlines():
    lst.append(line.split())


def count(string, nums):
    if string == "":
        if nums == ():
            return 1
        else:
            return 0
    if nums == ():
        if "#" in string:
            return 0
        else:
            return 1

    result = 0

    if string[0] in ".?":
        result += count(string[1:], nums)

    if string[0] in "#?":
        if int(nums[0]) <= len(string) and "." not in string[:int(nums[0])] and (int(nums[0]) == len(string) or string[int(nums[0])] != "#"):
            result += count(string[int(nums[0]) + 1:], nums[1:])
    return result


total = 0
i = 0
while i < len(lst):
    lst[i][1] = tuple(lst[i][1].split(","))
    i += 1

for line in lst:
    total += count(line[0], line[1])

print(total)