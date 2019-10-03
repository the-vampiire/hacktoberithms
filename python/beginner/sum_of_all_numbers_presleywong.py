def sum_all(input_list):
    if type(input_list) is not list:
       return

    total = 0
    input_list.sort()
    start = input_list[0]
    end = input_list[-1]+1

    for n in range(start, end):
        total += n

    return total
