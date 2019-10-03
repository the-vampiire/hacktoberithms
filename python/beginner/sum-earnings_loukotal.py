def sum_earning(input_str):
    nums = [n for n in input_str.split(",")]
    streak = 0
    for num in nums:
        if num.isalpha() or num.isspace() or num == "":
            return 0
        else:
            num = int(num)

        if num < 0 and streak + num <= 0:
    
            streak = 0
        else:
            streak += num

    return streak
    
# print(sum_earning(",,3,0,1,as,d"))
# print(sum_earning("3,3,3,3,3,-3"))
print(sum_earning("0,7,0,2,-12,3,0,2"))
print(sum_earning("qwerty"))
print(sum_earning(",,3,,4"))
print(sum_earning("1,2,v,b,3"))
print(sum_earning("1,3,-2,1,2"))