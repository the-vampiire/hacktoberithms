def sum_earnings(input):
    nums = [n for n in input.split(",")]
    soFar = 0
    for n in nums:
        if n.isalpha() or n.isspace() or n == "":
            return 0
        else:
            n = int(n)
        if n < 0 and soFar + n <= 0:
            soFar = 0
        else:
            soFar += n
    return soFar
    
