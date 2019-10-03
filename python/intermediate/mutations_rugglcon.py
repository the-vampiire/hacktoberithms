def mutations(words):
    for l in words[1].lower():
        try:
            words[0].lower().index(l, 0)
        except ValueError:
            return False
        return True
