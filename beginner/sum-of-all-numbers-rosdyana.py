
def sum_all(list_input):
    result = 0
    # find the max and min on the list
    firstnum = min(list_input)
    secondnum = max(list_input)
    # in case the list contain same number
    if list_input[0] == list_input[1]:
        return list_input[0]
    # start to sum it
    for i in range(firstnum, secondnum+1):
        result += i
    return result
