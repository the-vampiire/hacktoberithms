A="100000"
B="110000"
C="100100"
D="100110"
E="100010"
F="110100"
G="110110"
H="110010"
I="010100"
J="010110"
K="101000"
L="111000"
M="101100"
N="101110"
O="101010"
P="111100"
Q="111110"
R="111010"
S="011100"
T="011110"
U="101001"
V="111001"
W="010111"
X="101101"
Y="101111"
Z="101011"
space="000000"
zero="001011"
one="010000"
two="011000"
three="010010"
four="010011"
five="010001"
six="011010"
seven="011011"
eight="011001"
nine="001010"
exc="011101"
quote="000010"
pound="001111"
dlr="110101"
pct="100101"
ap="111101"
ast="100001"
plus="001101"
comma="000001"
minus="001001"
colon="100011"
scolon="000011"
fslash="001100"
lpar="111011"
rpar="011111"
per="000101"
equ="111111"
qst="100111"
bslash="110011"
ans=True
while ans==True:
    s=input("Please enter a string to translate to braille: ")
    s=s.upper()
    braille=""
    for x in range(len(s)):
        if s[x]=='A':
            braille+=A
        elif s[x]=='B':
            braille+=B
        elif s[x]=='C':
            braille+=C
        elif s[x]=='D':
            braille+=D
        elif s[x]=='E':
            braille+=E
        elif s[x]=='F':
            braille+=F
        elif s[x]=='G':
            braille+=G
        elif s[x]=='H':
            braille+=H
        elif s[x]=='I':
            braille+=I
        elif s[x]=='J':
            braille+=J
        elif s[x]=='K':
            braille+=K
        elif s[x]=='L':
            braille+=L
        elif s[x]=='M':
            braille+=M
        elif s[x]=='N':
            braille+=N
        elif s[x]=='O':
            braille+=O
        elif s[x]=='P':
            braille+=P
        elif s[x]=='Q':
            braille+=Q
        elif s[x]=='R':
            braille+=R
        elif s[x]=='S':
            braille+=S
        elif s[x]=='T':
            braille+=T
        elif s[x]=='U':
            braille+=U
        elif s[x]=='V':
            braille+=V
        elif s[x]=='W':
            braille+=W
        elif s[x]=='X':
            braille+=X
        elif s[x]=='Y':
            braille+=Y
        elif s[x]=='Z':
            braille+=Z
        elif s[x]==' ' or s[x]=='':
            braille+=space
        elif s[x]=='0':
            braille+=zero
        elif s[x]=='1':
            braille+=one
        elif s[x]=='2':
            braille+=two
        elif s[x]=='3':
            braille+=three
        elif s[x]=='4':
            braille+=four
        elif s[x]=='5':
            braille+=five
        elif s[x]=='6':
            braille+=six
        elif s[x]=='7':
            braille+=seven
        elif s[x]=='8':
            braille+=eight
        elif s[x]=='9':
            braille+=nine
        elif s[x]=='!':
            braille+=exc
        elif s[x]=='\"':
            braille+=quote
        elif s[x]=='#':
            braille+=pound
        elif s[x]=='$':
            braille+=dlr
        elif s[x]=='%':
            braille+=pct
        elif s[x]=='&':
            braille+=ap
        elif s[x]=='*':
            braille+=ast
        elif s[x]=='+':
            braille+=plus
        elif s[x]==',':
            braille+=comma
        elif s[x]=='-':
            braille+=minus
        elif s[x]==':':
            braille+=colon
        elif s[x]==';':
            braille+=scolon
        elif s[x]=='/':
            braille+=fslash
        elif s[x]=='(':
            braille+=lpar
        elif s[x]==')':
            braille+=rpar
        elif s[x]=='.':
            braille+=per
        elif s[x]=='=':
            braille+=equ
        elif s[x]=='?':
            braille+=qst
        elif s[x]=='\\':
            braille+=bslash
    print(braille)
    y=True
    while y == True:
        z=input("Do you have another string to translate? Enter (YES) or (NO): ")
        z=z.upper()
        if z == "YES":
            ans=True
            y=False
        elif z=="NO":
            ans=False
            y=False
            print("Thank you, goodbye!")
        else:
            print("Not a valid response.")
            y=True