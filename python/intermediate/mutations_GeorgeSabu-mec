def mutations(ls):
    #Changes strings to lowercase to compare case insensitive
    ls[0]=ls[0].lower()
    ls[1]=ls[1].lower()
    #Creates lists with the given strings
    str1 = list(ls[0])
    str2 = list(ls[1])
    #Loops through each character
    for i in ls[1]:
        #Checks if character is present in the first string
        if i in str1:
            #If its present , the character is removed from both the strings
            str1.remove(i)
            str2.remove(i)
    if len(str2)==0:
        return True
    else:
        return False


