import string

sum1 = 0
sum2 = 0
with open("input.txt", "r") as file:
    rucksack_no = 1
    rucksack1 = ""
    rucksack2 = ""
    rucksack3 = ""
    for line in file:
        line = line.strip()

        ## Part One
        compartment1 = line[:int((len(line)/2))]
        compartment2 = line[int((len(line)/2)):]
        common = ''
        for c in compartment1:
            if c in compartment2:
                common = c
                break
        if common.islower():
            sum1 += ord(common) - 96
        else:
            sum1 += ord(common) - 38

        ## Part Two
        if rucksack_no == 1:
            rucksack1 = line
            rucksack_no += 1
        elif rucksack_no == 2:
            rucksack2 = line
            rucksack_no += 1
        elif rucksack_no == 3:
            rucksack3 = line
            rucksack_no = 1

            badge = ''
            for c in rucksack1:
                if c in rucksack2 and c in rucksack3:
                    badge = c
                    break
            if badge.islower():
                sum2 += ord(badge) - 96
            else:
                sum2 += ord(badge) - 38

print(sum1)
print(sum2)
