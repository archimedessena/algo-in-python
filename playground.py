def smallest_number(num):
    small_num = num[0]
    for val in num:
        if val < small_num:
            small_num = val
        else:
            return "No small number"
    return small_num


print(smallest_number([5, 7, 9]))
