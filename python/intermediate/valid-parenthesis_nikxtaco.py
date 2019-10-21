def has_valid_parens(str):
    for i in range(len(str)):
        if "()" in str:
            str = str.replace("()", "")
        if "[]" in str:
            str = str.replace("[]", "")
        if "{}" in str:
            str = str.replace("{}", "")

    if len(str) == 0:
        return True
    return False

print(has_valid_parens('()'))  #True
print(has_valid_parens('()[]{}'))  #True
print(has_valid_parens('(]'))  #False
print(has_valid_parens('([)]'))  #False
print(has_valid_parens('{[]}'))  #True
