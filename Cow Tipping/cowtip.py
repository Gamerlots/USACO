with open("cowtip.in") as cowtip:
    LENGTH = int(cowtip.readline())

    grid = []
    for row in cowtip:
        row = row.strip()
        for column in row:
            grid.append(int(column))

flips = 0

def cow_tip(x_pos, y_pos):
    for position, number in enumerate(grid):
        if position % LENGTH <= x_pos and position // LENGTH <= y_pos:
            grid[position] = 1 - number

for position, number in enumerate(reversed(grid)):
    position = LENGTH ** 2 - position - 1
    if not any(grid):
        break
    if number == 1:
        flips += 1
        cow_tip(position % LENGTH, position // LENGTH)

with open("cowtip.out", "w") as cowtip:
    print(flips, file=cowtip)
