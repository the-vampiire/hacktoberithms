def answer(l):
    # Only one element
    if(len(l)==1):
        return l[0]

    zeros = 0 # Number of zeros
    neg = 0 # Number of negative numbers
    max_neg = -9999999 # Max negative number
    prod = 1 # Max product
    
    for i in l:
        if(i == 0):
            zeros += 1
        else:
            if(i < 0):
                neg += 1
                max_neg = max(i, max_neg)

            prod *= i

    # If all numbers are zeros, so return 0
    if(zeros == len(l)):
        return 0
    elif(neg%2 != 0): # Odd number of negative numbers
        # Only one negative number and the remainder are zeros
        if(zeros == len(l) - 1 and neg == 1):
            return 0
        
        prod = int(prod/max_neg) # Maximum product 
    
    return str(prod)

if __name__ == "__main__":
    # Tests cases
    tests = [
        [0, -4, -4],
        [0, -1, 0],
        [0],
        [0, -5],
        [2, 2, 0, 2,0],
        [2, -3, 1, 0, -5],
        [-2, -3, 4, -5],
    ]

    for t in tests: 
        print(answer(t))
