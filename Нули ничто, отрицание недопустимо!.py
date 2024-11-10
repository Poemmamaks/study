my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while True:
    m = my_list[i]
    i = i + 1
    if m > 0:
        print(m)
        continue
    else:
        if m < 0:
            break

