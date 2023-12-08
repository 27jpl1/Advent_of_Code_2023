import math

directions = open('Directions', 'r')
lst = []
total = 1
for line in directions.readlines():
    word = line.strip()
    lst.append(word)
instructions = []
for char in lst[0]:
    if char == "R":
        instructions.append(1)
    else:
        instructions.append(0)
directions_dict = {}
i = 2
while i < len(lst):
    directions_dict[lst[i][0:3]] = (lst[i][7:10], lst[i][12:15])
    i += 1
elements = []
for direction in directions_dict:
    if direction[2] == "A":
        elements.append(direction)
first_find = {}
i = 0
while i < len(elements):
    steps = 0
    while elements[i][2] != "Z":
        direction = instructions[steps % len(instructions)]
        elements[i] = directions_dict[elements[i]][direction]
        steps += 1
    first_find[elements[i]] = steps
    i += 1
lcm = math.lcm(first_find[elements[0]], first_find[elements[1]])
i = 2
while i < len(first_find):
    lcm = math.lcm(lcm, first_find[elements[i]])
    i += 1
print(lcm)
