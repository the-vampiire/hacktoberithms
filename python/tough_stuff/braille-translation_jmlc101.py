def alphaToBraille(inputString):
    braille = ['000000', '100000', '110000', '100100', '100110', '100010', '110100', '110110', '110010', '010100', '010110',
    '101000', '111000', '101100', '101110', '101010', '111100', '111110', '111010', '011100', '011110',
    '101001', '111001', '010111', '101101', '101111', '101011']
    alphabetKey = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    brailleUpper = list(map(lambda x : '000001' + x, braille))
    alphabetKeyUpper = list(map(lambda x : x.upper(), alphabetKey))
    lowercaseDict = dict(zip(alphabetKey, braille))
    uppercaseDict = dict(zip(alphabetKeyUpper, brailleUpper))
    tmp = []

    while True:
        try:
            for item in inputString:
                if item.islower():
                    tmp.append(lowercaseDict[item])
                elif item.isupper():
                    tmp.append(uppercaseDict[item])
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
