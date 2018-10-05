def mutation(s):
    alpha = []
    s[0] = s[0].lower()
    s[1] = s[1].lower()
    for i in range(2):
        alpha.append([0 for _ in range(26)])

    if(len(s[0]) < len(s[1])):
        return False

    for i in range(len(s[1])):
        alpha[0][ord(s[0][i])-97] += 1
        alpha[1][ord(s[1][i])-97] += 1
   
    for j in range(i, len(s[0])):
        alpha[0][ord(s[0][j])-97] += 1

    for i in range(26):
        if alpha[1][i] > alpha[0][i]:
            return False

    return True


Test = [["hello", "Hello"],
        ["hello", "hey"],
        ["Alien", "line"],
        ['hel', 'heel'],
        ['heloes', 'hello']]

for test in Test:
    print(mutation(test))
