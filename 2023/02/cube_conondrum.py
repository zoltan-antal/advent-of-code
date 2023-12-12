def line_to_draws(line):
    return line.split(": ")[1].split("; ")


def parse_draw(draw):
    colours = {}
    for item in draw.split(", "):
        item = item.split(" ")
        colours[item[1]] = int(item[0])
    return colours


with open("input.txt", "r") as fhand:
    lines = fhand.readlines()
lines = list(map(lambda line: line.strip(), lines))

games = list(map(lambda line: list(
    map(lambda draw: parse_draw(draw), line_to_draws(line))), lines))

bag = {"red": 12, "green": 13, "blue": 14}
sum_possible = 0
for index, game in enumerate(games, 1):
    possible = True
    for draw in game:
        for colour, value in draw.items():
            if bag[colour] < value:
                possible = False
        if not possible:
            break
    if possible:
        sum_possible += index
print("Part one:", sum_possible)

sum_power = 0
for game in games:
    colours = {"red": 1, "green": 1, "blue": 1}
    for draw in game:
        for colour, value in draw.items():
            if colours[colour] < value:
                colours[colour] = value
    power = colours["red"] * colours["green"] * colours["blue"]
    sum_power += power
print("Part two:", sum_power)
