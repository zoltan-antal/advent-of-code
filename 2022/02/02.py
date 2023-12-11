score1 = 0
score2 = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        played = line.split()
        if played[1] == 'X':
            score1 += 1
            score2 += 0
            if played[0] == 'A':
                score1 += 3
                score2 += 3
            if played[0] == 'B':
                score1 += 0
                score2 += 1
            elif played[0] == 'C':
                score1 += 6
                score2 += 2
        elif played[1] == 'Y':
            score1 += 2
            score2 += 3
            if played[0] == 'A':
                score1 += 6
                score2 += 1
            elif played[0] == 'B':
                score1 += 3
                score2 += 2
            elif played[0] == 'C':
                score1 += 0
                score2 += 3
        elif played[1] == 'Z':
            score1 += 3
            score2 += 6
            if played[0] == 'A':
                score1 += 0
                score2 += 2
            elif played[0] == 'B':
                score1 += 6
                score2 += 3
            elif played[0] == 'C':
                score1 += 3
                score2 += 1

print(score1)
print(score2)
