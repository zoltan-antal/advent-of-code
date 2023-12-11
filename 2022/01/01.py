elves = []

# with open("input.txt", "r") as file:
#     elf = []
#     for line in file:
#         line = line.strip()
#         if line != "":
#             elf.append(int(line))
#         else:
#             elves.append(elf)
#             elf = []

# # for elf in elves:
# #     for cal in elf:
# #         print(cal)
# #     print()

# max = 0
# for elf in elves:
#     sum = 0
#     for cal in elf:
#         sum += cal
#     if sum > max:
#         max = sum

# print(max)

max1 = 0
max2 = 0
max3 = 0
with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        line = line.strip()
        if line != "":
            sum += int(line)
        else:
            if sum > max1:
                max3 = max2
                max2 = max1
                max1 = sum
            elif sum > max2:
                max3 = max2
                max2 = sum
            elif sum > max3:
                max3 = sum
            sum = 0

print(max1)
print(max2)
print(max3)

print(max1 + max2 + max3)
