"""Solution for Issue #8 (Sum Earnings Challenge)."""


def sum_earnings(finance_data):
    """Validate and process input."""
    try:
        required_nums = finance_data.count(',') + 1
        history = list(map(int, finance_data.split(',')))
        if len(history) != required_nums:
            raise ValueError
        balance = 0
        for i in history:
            balance += i
            if balance < 0:
                balance = 0
        return balance
    except ValueError:
        return 0


print(sum_earnings(input()))
