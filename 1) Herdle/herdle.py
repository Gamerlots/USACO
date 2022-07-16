from operator import eq

a_grid = input() + input() + input()
g_grid = input() + input() + input()

green = sum(map(eq, a_grid, g_grid))
yellow = sum(min(a_grid.count(g), g_grid.count(g)) for g in {*g_grid}) - green

print(green, yellow, sep="\n")
