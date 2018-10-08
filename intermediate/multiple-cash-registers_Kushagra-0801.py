"""Solution to Issue #68 (Multiple Cash Registers)."""


def checkout_time(customers, cash_registers):
    """Find the time required for all the customers to checkout."""
    if len(customers) < cash_registers:
        return max(customers)

    cashiers = [customers[i] for i in range(cash_registers)]
    for i in customers[cash_registers:]:
        cashiers[cashiers.index(min(cashiers))] += i
    return max(cashiers)


def test():
    """Testing function."""
    test_cases = [
                  # ([5, 1, 3], 1, 9),
                  # ([10, 3, 4, 2], 2, 10),
                  ([100000-i for i in range(100000)], 100, 2)
                 ]
    tests_passed = True

    for i in test_cases:
        try:
            assert checkout_time(i[0], i[1]) == i[2]
        except AssertionError:
            tests_passed = False
            print(i, checkout_time(i[0], i[1]), sep='\t')
            continue

    if tests_passed:
        print('All Tests Passed.')
    else:
        print('All Tests NOT Passed.')


def main():
    """Actual Function."""
    customers = list(map(int, input().split()))
    cash_registers = int(input())
    print(checkout_time(customers, cash_registers))


if __name__ == '__main__':
    test()
