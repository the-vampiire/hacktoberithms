
def mutations(list_with_words):

        if len(list_with_words) == 2:

            word1 = list(list_with_words[0].lower())
            word2 = list(list_with_words[1].lower())

            for letter in set(word1):
                if letter not in word2:
                    return False
            return True


print(mutations(['teeSt', 'tste']), mutations(['wow', 'test']))
