input_list = []
for i in range(2):
    input_list.append(int(input("enter no: ")))


def sum_all(a):
    if a[0] > a[1]:
        a[0], a[1] = a[1], a[0]
    sum = 0
    for n in range(a[0], a[1] + 1):
        sum += n
    return sum


print(sum_all(input_list))