def valid_parens(string_of_parens):
    for i in range(len(string_of_parens)):
        if "()" in string_of_parens:
            string_of_parens = string_of_parens.replace("()", "")
        if "[]" in string_of_parens:
            string_of_parens = string_of_parens.replace("[]", "")
        if "{}" in string_of_parens:
            string_of_parens = string_of_parens.replace("{}", "")

    if len(string_of_parens) == 0:
        return True
    return False

print(valid_parens(''))  # Expected True
print(valid_parens('()'))  # Expected True
print(valid_parens('()[]{}'))  # Expected True
print(valid_parens('(]'))  # Expected False
print(valid_parens('([)]'))  # Expected False
print(valid_parens('{[]}'))  # Expected True
