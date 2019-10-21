"""
Challenge: Write a function that returns True if the first string in a list
contains all of the letters of the second string in the list.

Examples:
["hello", "hey"]
should return false because the string "hello" does not contain a "y".

["alien", "line"]
should return true because all of the letters in "line" are present in "Alien".
"""
        
def all_there():
    
    print("This function takes two words as input and checks to see if " +
          "all the letters in Word 2 are in Word 1.")
    
    strings = input("Enter two words, separated by a comma (no spaces): ").lower().split(',')
    word1 = strings[0]
    word2 = strings[1]

    print("You entered,", word1, " and", word2)

    for i in word2:
        if i in word1:
            return True
        else:
            return False
