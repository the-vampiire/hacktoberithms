import functools


def sum_earnings(s: str) -> int:
    """
    Challenge
    - Write a function that accepts a comma-separated string input of
    earning/spending activity and returns the sum of earnings as a
    single int value.

    - If at any point the spending (negative) value is greater than the
    sum of earned (positive) values before it then the streak ends and
    the count should start over

    We have a list in string type separated by commas that represented
    buy or sell activity. Positive value for selling and negative value
    for buying activity. For example, in the following string, this
    user sold something for $7 on the 2nd day, and something for $2 on
    the 4th day, and then bought something for $12 on the 5th day, and
    so on.

    >>> sum_earnings('0,7,0,2,-12,3,0,2')
    5

    This user's highest earnings streak is $5, which started on the 6th
    day and ended on the 8th day. The streak does not start before the
    6th day because the user spent $12 on the 5th and broke earlier
    streak on $9.

    >>> sum_earnings('1,3,-2,1,2')
    5


    notes
    If the user did not do anything (i.e. 0,0,0,0,0) or only bought
    things without selling anything (i.e. -4,-3,-7,-1), then it should
    output with 0.

    >>> sum_earnings('0,0,0,0,0')
    0

    >>> sum_earnings('-4,-3,-7,-1')
    0

    Your program should be able to handle a comma-separated string
    consisting of any number of values. Your program should also be
    able to handle invalid input. If an invalid input is given, it
    should output 0.

    some examples of invalid input:

    >>> sum_earnings('qwerty')
    0
    >>> sum_earnings(',,3,,4')
    0
    >>> sum_earnings('1,2,v,b,3')
    0
    """
    vals = map(int, s.split(','))

    try:
        return functools.reduce(lambda x, y: max(0, x + y), vals)
    except ValueError:
        return 0
