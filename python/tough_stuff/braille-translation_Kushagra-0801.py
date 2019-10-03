"""Solution to Issue #14 (Braille Translation)."""

braille_table = {
        'a': '100000',
        'b': '110000',
        'c': '100100',
        'd': '100110',
        'e': '100010',
        'f': '110100',
        'g': '110110',
        'h': '110010',
        'i': '010100',
        'j': '010110',
        'k': '101000',
        'l': '111000',
        'm': '101100',
        'n': '101110',
        'o': '101010',
        'p': '111100',
        'q': '111110',
        'r': '111010',
        's': '011100',
        't': '011110',
        'u': '101001',
        'v': '111001',
        'w': '010111',
        'x': '101101',
        'y': '101111',
        'z': '101011',
        ' ': '000000',
        'CAP': '000001',
        }

test_cases = {
        'code': '100100101010100110100010',
        'Braille': '000001110000111010100000010100111000111000100010',
        'The quick brown fox jumped over the lazy dog':
        '''00000101111011001010001000000011111010100101010010010010100000000011\
0000111010101010010111101110000000110100101010101101000000010110101001101100111\
1001000101001100000001010101110011000101110100000000111101100101000100000001110\
00100000101011101111000000100110101010110110'''
        }


def translate(string):
    """Translate plain-text to braille."""
    braille_code = []
    for i in string:
        if i.isupper():
            braille_code.append(braille_table['CAP'])
            braille_code.append(braille_table[i.lower()])
            continue
        braille_code.append(braille_table[i])
    return ''.join(braille_code)


def test():
    """Actual Function."""
    for item, value in test_cases.items():
        try:
            assert(translate(item) == value)
        except AssertionError:
            print(item, value, translate(item), sep='\n')
            continue
    print('Tests Passed.')


def main():
    """Actual Function."""
    string = input()
    print(translate(string))


if __name__ == '__main__':
    main()
