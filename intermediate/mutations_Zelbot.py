def mutations(string_list):
    # We assume that the string_list contains two strings
    letters = set(list(string_list[1].lower()))
    if all(letter in string_list[0].lower() for letter in letters):
        return True
    return False

print(mutations(["hello", "Hello"]))  # Expected True
print(mutations(["hello", "hey"]))  # Expected False
print(mutations(["Alien", "line"]))  # Expected True
