hashes = open('Hashes', 'r')
lst = []
total = 0
for line in hashes.readlines():
    word = line.strip()
    lst.append(word)
sequence = lst[0]
curr_val = 0
for char in sequence:
    if char == ",":
        total += curr_val
        curr_val = 0
    else:
        curr_val += ord(char)
        curr_val *= 17
        curr_val %= 256
total += curr_val
print(total)