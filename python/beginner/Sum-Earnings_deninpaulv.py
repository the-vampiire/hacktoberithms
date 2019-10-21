def sum_earnings(array):
    global highest_streak
    for item in range(0, len(array)):
        local_sum = 0
        for item in range(item, len(array)):
            local_sum += array[item]
            if local_sum < 0:
                break
        if local_sum > highest_streak:
            highest_streak = local_sum


arr = []
flag=0
highest_streak = 0
Input = str(input())

# making into array
temp = Input.split(",")
for i in temp:
    try:
        tempitem = int(i)
    except:
        flag+=1
    arr.append(tempitem)

if flag==0:
    sum_earnings(arr)
print(highest_streak)
