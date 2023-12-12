import re


def line_to_digits(line):
    digit_names = ["one", "two", "three", "four",
                   "five", "six", "seven", "eight", "nine"]
    digits = {}
    for value, digit_name in enumerate(digit_names, 1):
        for digit in [m.start() for m in re.finditer(digit_name, line)]:
            digits[digit] = str(value)

    for index, char in enumerate(line):
        if char.isnumeric():
            digits[index] = char

    digits_sorted = []
    for index in sorted(list(digits.keys())):
        digits_sorted.append(digits[index])

    return digits_sorted


with open("input.txt", "r") as fhand:
    lines = fhand.readlines()
lines = list(map(lambda line: line.strip(), lines))

lines_digits = list(map(lambda line: line_to_digits(line), lines))

numbers = list(map(lambda line: int(line[0] + line[-1]), lines_digits))

sum = sum(numbers)

print(sum)
