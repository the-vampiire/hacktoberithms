a = ["hello", "Hello"]
b = ["hello", "hey"]
c = ["Alien", "line"]

def mutations(lst):
    
    first = lst[0]
    print(first)
    second = lst[1]
    print(second)
    
    for char in second.lower():
        if char not in first.lower():
            return False
    return True

    
print(mutations(c))