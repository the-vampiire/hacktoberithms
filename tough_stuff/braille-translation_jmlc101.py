def alphaToBraille(inputString):
    d = {'a':'100000', 'b':'110000', 'c':'100100', 'd':'100110', 'e':'100010', 'f':'110100', 'g':'110110', 'h':'110010', 'i':'010100', 'j':'010110',
    'k':'101000', 'l':'111000', 'm':'101100', 'n':'101110', 'o':'101010', 'p':'111100', 'q':'111110', 'r':'111010', 's':'011100', 't':'011110',
    'u':'101001', 'v':'111001', 'w':'010111', 'x':'101101', 'y':'101111', 'z':'101011', 'A':'100000', 'B':'110000', 'C':'100100', 'D':'100110', 'E':'100010', 'F':'110100', 'G':'110110', 'H':'110010', 'I':'010100', 'J':'010110',
    'K':'101000', 'L':'111000', 'M':'101100', 'N':'101110', 'O':'101010', 'P':'111100', 'Q':'111110', 'R':'111010', 'S':'011100', 'T':'011110',
    'U':'101001', 'V':'111001', 'W':'010111', 'X':'101101', 'Y':'101111', 'Z':'101011', ' ':'000000'}
    tmp = []
    while True:
        try:
            for item in inputString:
                tmp.append(d[item])
            brailleString = ''.join(tmp)
            return brailleString
        except KeyError:
            print("\nAlphabetical characters only, please try again...\n")
            break
        

def main():
    toBeTranslated = input("\nEnter what you'd like to translate to Braille:")
    while True:
        isAlpha = ''
        for item in toBeTranslated:
            if (item == ' ') or (item.isalpha() == True):
                continue
            else:
                isAlpha = False

        if isAlpha == False:
            print("\nAlphabetical characters only, please try again...")
            toBeTranslated = input("\nEnter what you'd like to translate to Braille:")
        else:
            return print(alphaToBraille(toBeTranslated))
            
    

if __name__  == "__main__":
    main()
