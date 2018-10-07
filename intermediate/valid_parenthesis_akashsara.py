#!python3

def has_valid_parens(input_string):
	"""
	CHALLENGE: 
	Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

	An input string is valid if:
    > Open brackets must be closed by the same type of brackets.
    > Open brackets must be closed in the correct order.
    > Note that an empty string is also considered valid.

	DIFFICULTY: INTERMEDIATE [Due to use of stack]
	"""
	stack = []
	bracket_map = {'[':']',	'(':')', '{':'}'}
	for bracket in input_string:
		if bracket in bracket_map:
			stack.append(bracket)
		elif len(stack) == 0 or bracket_map[stack.pop()] != bracket:
			return False
	return len(stack) == 0