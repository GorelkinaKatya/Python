a = 6
b = 2
c = 10

i = 1
j = 0
part_a = 0
part_b = 0

if a < b:
    while part_a < a * b:
        part_a = a * i
        part_b = b * i
        if c == part_a or c == part_b:
            j = j + 1
        i = i + 1
else:
    while part_b < a * b:
        part_a = a * i
        part_b = b * i
        if c == part_a or c == part_b:
            j = j + 1
        i = i + 1

if j == 0:
    print('no')
else:
    print('yes')