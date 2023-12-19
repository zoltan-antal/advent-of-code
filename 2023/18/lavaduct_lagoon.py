with open("input.txt", "r") as fhand:
    lines = fhand.readlines()
lines = [line.strip() for line in lines]

dig_plan = []
for line in lines:
    values = line.split()
    dig_plan.append({"dir": values[0], "len": int(
        values[1]), "col": values[2][1:-1]})

x = 0
y = 0
grid_init = {}
for op in dig_plan:
    for i in range(op["len"]):
        grid_init[(x, y)] = op["col"]
        match op["dir"]:
            case "R":
                x += 1
            case "L":
                x -= 1
            case "U":
                y += 1
            case "D":
                y -= 1

x_min = min(x for x, y in grid_init.keys())
y_min = min(y for x, y in grid_init.keys())
x_max = max(x for x, y in grid_init.keys())
y_max = max(y for x, y in grid_init.keys())

x_total = x_max - x_min + 1
y_total = y_max - y_min + 1

grid = [['.' for y in range(y_total)] for x in range(x_total)]

for (x, y), value in grid_init.items():
    grid[x - x_min][y - y_min] = "#"

for y in range(y_total - 1, -1, -1):
    trenches = []
    trench_found = False
    for x in range(x_total):
        if grid[x][y] != '#':
            if trench_found:
                trench_found = False
                trenches[-1]["end"] = x - 1
            continue
        if not trench_found:
            trench_found = True
            trenches.append({"start": x, "valid": False})
        if x == x_total - 1:
            trenches[-1]["end"] = x
    for trench in trenches:
        above = False
        below = False
        for x in range(trench["start"], trench["end"] + 1):
            if y < y_total - 1:
                if grid[x][y + 1] == '#':
                    above = True
            if y > 0:
                if grid[x][y - 1] == '#':
                    below = True
        if above and below:
            trench["valid"] = True
    fill = False
    for index, trench in enumerate(trenches):
        if fill:
            for x in range(trenches[index - 1]["end"] + 1, trench["start"]):
                grid[x][y] = '*'
        if trench["valid"]:
            fill = not fill


sum = 0
fhand = open("output.txt", "w")
for y in range(y_total - 1, -1, -1):
    for x in range(x_total):
        if grid[x][y] != '.':
            sum += 1
        fhand.write(grid[x][y])
    fhand.write("\n")
fhand.close()
print(sum)
