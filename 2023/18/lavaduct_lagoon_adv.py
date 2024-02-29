with open("input.txt", "r") as fhand:
    lines = fhand.readlines()
lines = [line.strip() for line in lines]

dig_plan = []
dir_codes = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
x = 0
y = 0
x_min = 0
y_min = 0
for line in lines:
    values = line.split()
    col = values[2][2:-1]
    dir = dir_codes[col[-1]]
    len = int(col[:-1], 16)
    start = (x, y)
    match dir:
        case "R":
            x += len
        case "L":
            x -= len
        case "U":
            y += len
        case "D":
            y -= len
    if x < x_min:
        x_min = x
    if y < y_min:
        y_min = y
    end = (x, y)
    dig_plan.append({"dir": dir, "len": len, "start": start, "end": end})

for section in dig_plan:
    x_start, y_start = section["start"]
    x_end, y_end = section["end"]
    x_start -= x_min
    x_end -= x_min
    y_start -= y_min
    y_end -= y_min
    section["start"] = (x_start, y_start)
    section["end"] = (x_end, y_end)

area = 0
circumference = 0
for section in dig_plan:
    circumference += section["len"]
    dir = section["dir"]
    if not dir in ["U", "D"]:
        continue
    x_start, y_start = section["start"]
    x_end, y_end = section["end"]
    d = x_start * (y_start - y_end)
    area += d

area_total = int(area + (circumference / 2) + 1)
print(area_total)
