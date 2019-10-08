input_list = []
n = int(input("enter no of panels: "))
for i in range(n):
    input_list.append(int(input("enter power of panel: ")))


def answer(xs):
    neg = []
    pos = []
    max_pow = 1
    for power in xs:
        if power < 0:
            neg.append(power)
        elif power > 0:
            pos.append(power)
    if len(neg) % 2 != 0:
            neg.remove(max(neg))
    for power in pos:
        max_pow *= power
    for power in neg:
        max_pow *= power
    return str(max_pow)


print(answer(input_list))