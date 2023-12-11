count1 = 0
count2 = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        (first, second) = line.split(',')
        (first_start, first_end) = map(int, first.split('-'))
        (second_start, second_end) = map(int, second.split('-'))

        ## Part One
        if (first_start >= second_start and first_end <= second_end) \
            or (second_start >= first_start and second_end <= first_end):
            count1 += 1

        ## Part Two
        if (second_start <= first_start <= second_end) \
            or (first_start <= second_start <= first_end):
            count2 += 1
            
print(count1)
print(count2)
