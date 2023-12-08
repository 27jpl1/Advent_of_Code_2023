directions = open('Directions', 'r')
lst = []
total = 1
for line in directions.readlines():
    word = line.strip()
    lst.append(word)
print(lst)
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
element = "AAA"
steps = 0
while element != "ZZZ":
    print(element)
    direction = instructions[steps % len(instructions)]
    element = directions_dict[element][direction]
    steps += 1
print(steps)