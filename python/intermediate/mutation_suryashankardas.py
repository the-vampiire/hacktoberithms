input_list = []
for i in range(2):
    input_list.append(input("enter word: "))

def mutation(a):
    count = 0
    for ch in a[1]:
        if ch not in a[0]:
            count = 1
    if count == 0:
        return True
    else:
        return False

print(mutation(input_list))