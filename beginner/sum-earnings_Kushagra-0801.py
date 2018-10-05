"""Solution for Issue #8 (Sum Eanings Challenge)."""

try:
    input_ = input()
    required_nums = input_.count(',') + 1
    history = list(map(int, input_.split(',')))
    if len(history) != required_nums:
        raise ValueError
    balance = 0
    for i in history:
        balance += i
        if balance < 0:
            balance = 0
    print(balance)
except ValueError:
    print('0')
