with open("input.txt", "r") as fhand:
    lines = fhand.readlines()
lines = [line.strip() for line in lines]

lines_digits = list(map(lambda line: list(
    filter(lambda char: char.isnumeric(), list(line))), lines))

numbers = list(map(lambda line: int(line[0] + line[-1]), lines_digits))

sum = sum(numbers)

print(sum)
