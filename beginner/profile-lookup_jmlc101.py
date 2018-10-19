contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"]
    },
    {
        "firstName": "Harry",
        "lastName": "Potter",
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["JavaScript", "Gaming", "Foxes"]
    }
]


def look_up_profile(name, field):
    returns = ["No such contact", "No such property"]
    returned = ""
    contactFirstNames = []
    firstNameIndex = ""
    contactLastNames = []
    nameMatch = 0
    
    profileIndex = ""

    for item in contacts:
        contactFirstNames.append(item["firstName"])

    for firstName in contactFirstNames:
        if firstName == name:
            firstNameIndex = firstName.index()
            nameMatch += 1

    if nameMatch > 1:
        inputLastName = input("Enter the last name:")
        for item in contacts:
            contactLastNames.append(item["lastName"])
        for lastName in contactLastNames:
            if lastName == inputLastName and contactFirstNames[lastName.index()] == name:
                profileIndex = lastName.index()
    else:
        profileIndex = firstNameIndex
    
    # TODO - ADD "try" statement here in case field does not exist.
    if nameMatch >= 1:
        returned = contacts[profileIndex][field]
    elif nameMatch == 0:
        returned = returns[0]
    # except:
    # returned = returns[1]

    return returned
                
def main():
    #userInputFirstName = input("(Look up profile) Enter the first-name associated with profile:")
    #userInputField = input("Enter a field: \n(ex: lastName, number, likes)")

    print(contacts[1]["firstName"]) # Harry
    
'''
We have a list of dictionaries representing different people in our contacts list.

Complete the look_up_profile() function that takes name and a field as arguments included below

The function should check if name is an actual contact's firstName and the given field exists in that contact dictionary.

If both are true, then return the "value" of that field.

If name does not correspond to any contacts then return "No such contact"

If the field does not correspond to any valid properties of a contact found to match name then return "No such property"
'''


if __name__ == "__main__":
    main()

#look_up_profile("Akira", "likes")