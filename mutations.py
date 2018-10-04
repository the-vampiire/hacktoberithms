def mutations(words):
    for l in words[1]:
        try:
            "".lower().index(l)
        except ValueError:
            return False
        return True