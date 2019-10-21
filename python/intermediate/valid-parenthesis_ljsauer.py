"""
Challenge: Given a string containing only one or more from "()[]{}"
as input, determine if the input string is valid.
Input is valid if:
> Open brackets are closed by the same type of bracket
> Open brackets are closed in the correct order
> Input is empty
"""
def is_valid():
    string = input("Enter some parentheses: ")

    numOpen_p = 0
    numClosed_p = 0
    numOpen_k = 0
    numClosed_k = 0
    numOpen_c = 0
    numClosed_c = 0
        
    for char in string:
        if char == '(':
            numOpen_p +=1
            if numClosed_p > numOpen_p:
                return False
        elif char == '[':
            numOpen_k +=1
            if numClosed_k > numOpen_k:
                return False
        elif char == '{':
            numOpen_c +=1
            if numClosed_c > numOpen_c:
                return False
        elif char == ')':
            numClosed_p +=1
            if numClosed_p >= numOpen_p:
                return False
        elif char == ']':
            numClosed_k +=1
            if numClosed_k >= numOpen_k:
                return False
        elif char == '}':
            numClosed_c +=1
            if numClosed_c >= numOpen_c:
                return False
        elif string == '':
            return True

    if numOpen_p > numClosed_p:
        return False
    elif numOpen_k > numClosed_k:
        return False
    elif numOpen_c > numClosed_c:
        return False
    else:
        return True



