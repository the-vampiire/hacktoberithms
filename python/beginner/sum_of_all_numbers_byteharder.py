def sum_all(l):
    try:
        if len(l) > 2 or len(l) is 0:
            raise ValueError('List must have only 2 number exactly')

        if int(l[0]) == int(l[1]):
            return int(l[0]) + int(l[1])

        total_sum = 0
        if int(l[1]) > int(l[0]):
            return total_sum + sum_loop(int(l[0]), int(l[1]))
        return total_sum + sum_loop(int(l[1]), int(l[0]))
    except Exception as e:
        print(e.args)


def sum_loop(start_number, end_number):
    curr_sum = 0
    while int(start_number) <= int(end_number):
        curr_sum = curr_sum+int(start_number)
        start_number += 1
    return curr_sum
