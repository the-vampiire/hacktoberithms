
def sum_all(ls):
    sum = 0

    if(len(ls) != 2):
        print("Invalid input")

    else:
        ls.sort()
        start = ls[0]
        end = ls[1]
        
        if(start == end):
            sum = 2 * start
        
        else:
            for i in range(start, end+1):
                sum += i
    
    return sum
