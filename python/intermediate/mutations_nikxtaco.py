def mutations(mylist):

        if len(mylist) == 2:

            word1 = list(mylist[0].upper())
            word2 = list(mylist[1].upper())

            for letter in set(word1):
                if letter not in word2:
                    return False
            return True          

print(mutations(['hello', 'Hello']), mutations(['hello', 'hey']))
