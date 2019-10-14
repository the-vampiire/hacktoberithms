def sum_earnings(input):
    earning=0
    #Converts input string to list of strings
    strlist=input.split(",")
    intlist=[]
    #Loop for creating a list of integers from the list of strings
    for j in strlist:
        try:
            intlist.append(int(j))
        except:
            #Returns 0 if any character inserted in the list is not an integer
            return 0
    for i in intlist:
        earning+=i
        #Resets the streak if the earnings become less than the  spendings
        if(earning<0):
            earning=0
    return earning

if __name__=="__main__":
    str=input()
    print(sum_earnings(str))
