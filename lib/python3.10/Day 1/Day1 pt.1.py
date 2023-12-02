calories = open('Numbers', 'r')
lst = []
i = 0
first = 0
second = 0
total = 0
for line in calories.readlines():
    word = line.strip()
    lst.append(word)

while i < len(lst):
    first = 0
    second = 0
    first_taken = False
    second_taken = False
    for char in lst[i]:
        if char.isdigit():
            if not first_taken:
                first = int(char)
                first_taken = True
            elif not second_taken:
                second = int(char)
            else:
                pass
    if second == 0:
        second = int(first)
    total += first * 10 + second
    i += 1
print(total)
