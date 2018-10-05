"""
Write a function that satisfies the following rules:

Return true if the string in the first element of the list contains all of the letters of the string in the second element of the list.
"""

def mutation(input_list):
    short, long = sorted(map(lambda l: l.lower(), input_list), key=lambda item: len(item))
    for letter in short:
        if letter not in long:
            return False
    return True


if __name__ == "__main__":
    print(mutation(["hello", "Hello"]))
    print(mutation(["hello", "hey"]))
    print(mutation(["Alien", "line"]))
    print(mutation(["aaaaa", "aaaa"]))