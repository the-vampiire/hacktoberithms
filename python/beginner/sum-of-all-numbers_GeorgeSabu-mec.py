def sum_all(list):
    if(len(list) != 2):
        print("Invalid input")
    else:
        sum=list[0]+list[1]
#gets the highest and lowest of the two numbers
        if list[0]>list[1]:
            high,low=list[0],list[1]
        else:
            high,low=list[1],list[0]

#adds the numbers between the numbers low and high
        for i in range(low+1,high):
            sum+=i
        return sum

if __name__=="__main__":
    print(sum_all([1,3]))
