with open("input.txt", "r") as fhand:
    lines = fhand.readlines()
lines = [line.strip() for line in lines]

winning, guessed = zip(*[[[int(n) for n in numbers.split()]
                       for numbers in line.split(":")[1].split("|")] for line in lines])

sum_points = 0
for i in range(len(lines)):
    matches = len(set(winning[i]) & set(guessed[i]))
    if matches > 0:
        sum_points += 2 ** (matches - 1)
print("Part one:", sum_points)

cards = [1] * len(lines)
for i in range(len(lines)):
    matches = len(set(winning[i]) & set(guessed[i]))
    for shift in range(1, matches + 1):
        cards[i + shift] += cards[i]
sum_cards = sum(cards)
print("Part two:", sum_cards)
