last_chars = ""
char_no = 0
marker_len = 14
is_found = False
check = False

with open("input.txt", "r") as file:
    while True:
        char = file.read(1)

        if not char:
            break

        if char_no < marker_len and not check:
            last_chars = last_chars + char
            if char_no == marker_len - 1:
                check = True
        
        if check:
            last_chars = last_chars[1:] + char
            is_found = True
            for i in range(marker_len - 1):
                if last_chars[i] in last_chars[(i + 1):]:
                    is_found = False
        
        char_no += 1

        if is_found:
            print(char_no)
            break

# n = 14
# last_n = list()
# marker = 1

# with open("input.txt", "r") as file:
#     while True:
#         char = file.read(1)

#         last_n.append(char)
#         if marker > n:
#             last_n = last_n[1:]
#             if len(set(last_n)) == n:
#                 break

#         marker += 1

# print(marker)


