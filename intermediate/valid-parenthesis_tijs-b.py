def has_valid_parens(string):
    stack = []
    for character in string:
        if character == "(":
            stack.append("(")
        elif character == ")":
            if stack.pop() != "(":
                return False

        if character == "[":
            stack.append("[")
        elif character == "]":
            if stack.pop() != "[":
                return False

        if character == "{":
            stack.append("{")
        elif character == "}":
            if stack.pop() != "{":
                return False

    return len(stack) == 0

if __name__ == "__main__":
    assert has_valid_parens("()")
    assert has_valid_parens("()[]{}")
    assert has_valid_parens("{[]}")
    assert not has_valid_parens("(]")
    assert not has_valid_parens("([)]")
