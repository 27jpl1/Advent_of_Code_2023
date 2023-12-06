races = open('Races', 'r')
lst = []
total = 0
for line in races.readlines():
    word = line.strip()
    lst.append(word)
split_lst = []
for line in lst:
    split_lst.append(line.split())
index = 1
race_time = ""
race_distance = ""
while index < len(split_lst[0]):
    race_time += split_lst[0][index]
    race_distance += split_lst[1][index]
    index += 1
print("race_time", race_time)
time_pressed = 0
while time_pressed < int(race_time):
    print("time_pressed", time_pressed)
    movement_time = int(race_time) - time_pressed
    distance = time_pressed * movement_time
    if distance > int(race_distance):
        total += 1
    time_pressed += 1
print(total)