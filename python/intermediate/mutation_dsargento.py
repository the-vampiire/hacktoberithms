def mutation(word_list):
    if all(i in word_list[0].lower() for i in word_list[1].lower()):
        return True
    return False


print(mutation(["hello", "Hello"]))
print(mutation(["hello", "hey"]))
print(mutation(["Alien", "line"]))
