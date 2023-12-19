with open("input.txt", "r") as fhand:
    lines = fhand.readlines()
lines = [line.strip() for line in lines]

numbers = []
symbols = []
for line in lines:
    numbers.append([])
    symbols.append([])
    number_found = False
    for char_index, char in enumerate(line):
        if char == ".":
            number_found = False
            continue
        if not char.isnumeric():
            number_found = False
            symbols[-1].append(char_index)
            continue
        if not number_found:
            number_found = True
            numbers[-1].append({"number": 0, "index": char_index})
        numbers[-1][-1]["number"] = numbers[-1][-1]["number"] * \
            10 + int(char)

sum_parts = 0
for line_index, line in enumerate(numbers):
    for number in line:
        is_part = False
        start = number["index"]
        end = start + len(str(number["number"]))
        if (start - 1) in symbols[line_index] or end in symbols[line_index]:
            is_part = True
        if (line_index > 0) and any((start - 1) <= i <= end for i in symbols[line_index - 1]):
            is_part = True
        if (line_index < len(symbols) - 1) and any((start - 1) <= i <= end for i in symbols[line_index + 1]):
            is_part = True
        if is_part:
            sum_parts += number["number"]
print("Part one:", sum_parts)

sum_gears = 0
for line_index, line in enumerate(symbols):
    for gear_index in line:
        if lines[line_index][gear_index] != "*":
            continue
        adjacent_numbers = []
        for number in (n["number"] for n in numbers[line_index] if ((n["index"] + len(str(n["number"]))) == gear_index) or (n["index"] - 1 == gear_index)):
            adjacent_numbers.append(number)
        if (line_index > 0):
            for number in (n["number"] for n in numbers[line_index - 1] if (n["index"] - 1) <= gear_index <= n["index"] + len(str(n["number"]))):
                adjacent_numbers.append(number)
        if (line_index < len(numbers) - 1):
            for number in (n["number"] for n in numbers[line_index + 1] if (n["index"] - 1) <= gear_index <= n["index"] + len(str(n["number"]))):
                adjacent_numbers.append(number)
        if len(adjacent_numbers) == 2:
            sum_gears += adjacent_numbers[0] * adjacent_numbers[1]
print("Part two:", sum_gears)
