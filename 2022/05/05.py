stack_count = 0
is_read = False
stacks_a = dict()
stacks_b = dict()

with open("input.txt", "r") as file:
    for line in file:
        if stack_count == 0:
            stack_count = int(round((len(line) + 1)/4))
            for i in range(1, stack_count + 1):
                stacks_a[i] = []
                stacks_b[i] = []

        if not is_read:
            if line.strip()[0] != "[":
                is_read = True
                continue

            stack_no = 1
            line_segment = line
            while len(line_segment) >= 4:
                if line_segment[1] != " ":
                    stacks_a[stack_no].append(line_segment[1])
                    stacks_b[stack_no].append(line_segment[1])
                stack_no += 1
                line_segment = line_segment[4:]

        elif is_read and len(line.strip()) != 0:
            words = line.strip().split()
            to_move = int(words[1])
            from_stack = int(words[3])
            to_stack = int(words[5])
            
            for i in range(to_move):
                stacks_a[to_stack] = stacks_a[from_stack][0:1] + stacks_a[to_stack]
                stacks_a[from_stack] = stacks_a[from_stack][1:]

            stacks_b[to_stack] = stacks_b[from_stack][0:to_move] + stacks_b[to_stack]
            stacks_b[from_stack] = stacks_b[from_stack][to_move:]

print(stacks_a)
print(stacks_b)
for i in range(1, stack_count + 1):
    print(stacks_a[i][0], end="")

print()

for i in range(1, stack_count + 1):
    print(stacks_b[i][0], end="")
