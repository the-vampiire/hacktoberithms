def checkout_time(customers: list, cash_registers: int):
    if cash_registers == 1:
        return sum(customers)
    elif len(customers) <= cash_registers:
        return max(customers)

    registers = {}
    for i in range(cash_registers):
        registers[i] = customers.pop(0)

    iterations = 0
    while any(registers.values()):
        for r in registers.copy():

            registers[r] -= 1
            if registers[r] <= 0:
                try:
                    registers[r] = customers.pop(0)
                except IndexError:
                    registers[r] = 0

        iterations += 1

    return iterations


assert checkout_time([5, 1, 3], 1) == 9
assert checkout_time([10, 3, 4, 2], 2) == 10
assert checkout_time([8, 2, 3, 9], 3) == 11
assert checkout_time([8, 2, 9, 3], 5) == 9
assert checkout_time([4, 5, 6], 2) == 10
