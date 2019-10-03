def answer(panels):
    max_power = 1

    panels.sort()
    index = 0

    while index < len(panels):
        if panels[index] > 0:
            max_power = max_power * panels[index]
            index += 1
        elif panels[index] < 0:
            if (index + 1 < len(panels)) and panels[index + 1] < 0:
                max_power = max_power * panels[index] * panels[index + 1]
                index += 2
            else:
                index += 1
        else:
            index += 1

    return max_power


tests = [[-2, -3, 4, -5], [2, 0, 2, 2, 0], [-3, -4, -5, -6, -7]]

for test in tests:
    print(answer(test))
