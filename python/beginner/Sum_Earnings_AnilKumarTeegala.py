def Sum_Earnings(earnings):
    total_earnings=0 # Initialise total earnings to zero
    for money in earnings:
        if money < 0 and money + total_earnings < 0: #if sold+bought<0 and day_earnings<0 
                total_earnings = 0 #then assign total_earnings to zero
        else: #
            total_earnings += money # else add day_earnings to total_earnings
    return total_earnings # return total_earnings

inp=input().split(',') # input taken as comma separated string and converted into list
try:
    intInp = list(map(lambda x:int(x),inp)) # Converted list of String integers to Integers, if any alphabets got it catches the ValueError
    print(Sum_Earnings(intInp)) # if input contains all the string of integers then it goes to calculate total_earnings
except ValueError:
    print(0) # if input contains any albhabets then total earnings is Zero
