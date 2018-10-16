# > Credit: [adapted from Free Code Camp](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/mutations/)
# > # Challenge
# >
# > Write a function that satisfies the following rules:
# >
# >     * Return true if the string in the first element of the list contains all of the letters of the string in the second element of the list.
# >
# >
# > ## examples
# >
# > `["hello", "Hello"]`
# >
# >     * should return true because all of the letters in the second string are present in the first, ignoring case.
# >
# >
# > `["hello", "hey"]`
# >
# >     * should return false because the string "hello" does not contain a "y".
# >
# >
# > `["Alien", "line"]`
# >
# >     * should return true because all of the letters in "line" are present in "Alien".


def mutation(word_list):
    if all(i in word_list[0].lower() for i in word_list[1].lower()):
        return True
    return False


print(mutation(["hello", "Hello"]))
print(mutation(["hello", "hey"]))
print(mutation(["Alien", "line"]))
