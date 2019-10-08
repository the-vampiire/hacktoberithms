def has_valid_parens(text):
    """
    Checks if an input string contains valid parenthesis patterns.
    
    :param text: input string
    :return: boolean (True if the parentheses are valid, False otherwise)
    """
    for i in range(len(text)):
        text = text.replace('()', '').replace('{}', '').replace('[]', '')
    if not text:
        return True
    return False
    
print(has_valid_parens("()"))
#expected True
print(has_valid_parens("()[]{}"))
#expected True
print(has_valid_parens("(]"))
#expexted False
print(has_valid_parens("([)]"))
#expected False
print(has_valid_parens("{[]}"))
#expected True