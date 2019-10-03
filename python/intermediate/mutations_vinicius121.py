from collections import Counter

a = ["hello", "Hello"]
b = ["hello", "hey"]
c = ["Alien", "line"]
d = ["Hello","heel"]

def mutations(lst):
    
    first = lst[0].lower()
    second = lst[1].lower()
    
    counter_first = Counter(first)
    counter_second = Counter(second)
   
    for char in counter_second: 
        if counter_first[char] != counter_second[char]:
            return False

    return True
 
    
print(mutations(d))