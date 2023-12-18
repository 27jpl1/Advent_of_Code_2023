hashes = open('Hashes', 'r')
lst = []
total = 0
for line in hashes.readlines():
    word = line.strip()
    lst.append(word)
sequence = lst[0]
boxes = {}
equals = False
curr_val = 0
label = ""
for char in sequence:
    if equals:
        if curr_val in boxes.keys():
            set = False
            i = 0
            while i < len(boxes[curr_val]):
                if label == boxes[curr_val][i][0]:
                    boxes[curr_val][i][1] = char
                    set = True
                i += 1
            if not set:
                boxes[curr_val].append([label, char])
        else:
            boxes[curr_val] = [[label, char]]
        equals = False
    elif char == ",":
        curr_val = 0
        label = ""
    elif char == "=":
        equals = True
    elif char == "-":
        if curr_val in boxes.keys():
            i = 0
            while i < len(boxes[curr_val]):
                if label == boxes[curr_val][i][0]:
                    boxes[curr_val].remove(boxes[curr_val][i])
                    i = len(boxes)
                i += 1
    else:
        label += char
        curr_val += ord(char)
        curr_val *= 17
        curr_val %= 256
for box in boxes:
    if len(boxes[box]) == 0:
        pass
    else:
        i = 0
        while i < len(boxes[box]):
            total += (box + 1) * (i + 1) * int(boxes[box][i][1])
            i += 1
print(total)