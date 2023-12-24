from heapq import heappop, heappush

crucible = open('Crucible', 'r')
lst = []

for line in crucible.readlines():
    word = line.strip()
    temp_list = []
    for char in word:
        temp_list.append(int(char))
    lst.append(temp_list)

seen = []
heap = [(0, 0, 0, 0, 0, 0)]

while len(heap) > 0:
    spot = heappop(heap)
    heat = spot[0]
    row = spot[1]
    col = spot[2]
    row_movement = spot[3]
    col_movement = spot[4]
    times_in_direction = spot[5]

    if row == len(lst) - 1 and col == len(lst[0]) - 1:
        print(heat)
        break
    if (row, col, row_movement, col_movement, times_in_direction) in seen:
        pass
    else:
        seen.append((row, col, row_movement, col_movement, times_in_direction))
        if times_in_direction < 3 and (row_movement, col_movement) != (0, 0):
            new_row = row + row_movement
            new_col = col + col_movement
            if 0 <= new_row < len(lst) and 0 <= new_col < len(lst[0]):
                heappush(heap, (heat + lst[new_row][new_col], new_row, new_col, row_movement, col_movement, times_in_direction + 1))

        new_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for direction in new_directions:
            if (direction[0], direction[1]) != (row_movement, col_movement) and (direction[0], direction[1]) != (-row_movement, -col_movement):
                new_row = row + direction[0]
                new_col = col + direction[1]
                if 0 <= new_row < len(lst) and 0 <= new_col < len(lst[0]):
                    heappush(heap, (heat + lst[new_row][new_col], new_row, new_col, direction[0], direction[1], 1))


