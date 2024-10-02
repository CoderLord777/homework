my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
dist = int(len(my_list))
while dist > 0:
    if my_list[i] < 0:
        break
    print(my_list[i])
    dist -= 1
    i += 1
