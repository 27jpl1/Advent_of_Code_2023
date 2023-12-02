number_file = open('Numbers', 'r')
lst = []
i = 0
first = 0
second = 0
total = 0
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
dict = {"one" : 1, "two" : 2, "three" : 3, "four": 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
last_num = {"last_num" : 0}
for line in number_file.readlines():
    word = line.strip()
    lst.append(word)
while i < len(lst):
    first = 0
    second = 0
    first_taken = False
    second_taken = False
    chars = ""
    number_list = []
    for char in lst[i]:
        if len(chars) == 5:
            chars = chars[1:]
        chars += char
        for number in numbers:
            if number in chars:
                if not first_taken:
                    first = dict[number]
                    first_taken = True
                    chars = ""
                    last_num["last_num"] = first
                elif not second_taken:
                    if chars == "twone":
                        second = 1
                    else:
                        second = dict[number]
                    last_num["last_num"] = second
                else:
                    pass
        if char.isdigit():
            if not first_taken:
                first = int(char)
                first_taken = True
                chars = ""
                last_num["last_num"] = first
            elif not second_taken:
                second = int(char)
                chars = ""
                last_num["last_num"] = second
            else:
                pass
    if second == 0:
        second = last_num["last_num"]
    total += first * 10 + second
    i += 1
print(total)
