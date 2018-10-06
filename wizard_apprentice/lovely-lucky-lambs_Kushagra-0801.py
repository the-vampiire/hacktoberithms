"""Solution for Issue #15 (Lovely Lucky Lambs)."""

from functools import lru_cache


@lru_cache(maxsize=None)
def fib_num(n):
    """Return the nth fibonacci number. Use functool memoization."""
    if n == 1 or n == 2:
        return 1
    else:
        return fib_num(n-2) + fib_num(n-1)


def most_stingy(max_lambs):
    """Find number of henchmen accomodated when captain is most stingy."""
    lambs_given = 0             # When no lambs have been given,
    number_of_henchmen = 0      # no of henchmen in squad is also 0.
    while lambs_given <= max_lambs:
        number_of_henchmen += 1
        lambs_given += fib_num(number_of_henchmen)
    return (number_of_henchmen - 1)  # -1 because one hechman was added extra.


def most_generous(max_lambs):
    """Find number of henchmen accomodated when captain is most generous."""
    number_of_henchmen = max_lambs.bit_length() - 1  # Repeatedly divide by 2.
    return number_of_henchmen


def answer(total_lambs):
    """Call most_stingy and most_generous to calculate the answer."""
    return most_stingy(total_lambs) - most_generous(total_lambs)


def main():
    """Actual function."""
    total_lambs = int(input())
    print(answer(total_lambs))


if __name__ == '__main__':
    main()
