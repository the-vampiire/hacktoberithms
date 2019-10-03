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
        "firstName": "Harry",
        "lastName": "Pottey",
        "number": "0994372684222",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["JavaScript", "Gaming", "Foxes"]
    }
]


def look_up_profile(name, field):
    returns = ["No such contact", "No such property", "Last name not found"]
    returned = ""
    contactFirstNames = []
    contactLastNames = []
    nameMatch = 0
    profileIndex = 0

    for item in contacts:
        contactFirstNames.append(item["firstName"])

    for firstName in contactFirstNames:
        if firstName == name:
            profileIndex = contactFirstNames.index(firstName)
            nameMatch += 1

    if nameMatch > 1:
        matchCount = 0
        inputLastName = input("\nEnter the last name:")
        for item in contacts:
            contactLastNames.append(item["lastName"])
        for lastName in contactLastNames:
            if lastName == inputLastName and contactFirstNames[contactLastNames.index(lastName)] == name:
                profileIndex = contactLastNames.index(lastName)      
                matchCount += 1
        if matchCount < 1:
            return returns[2]
            
    try:
        if nameMatch >= 1:
            returned = contacts[profileIndex][field]
        elif nameMatch == 0:
            returned = returns[0]
    except KeyError:
        returned = returns[1]

    return returned
                
def main():
    userInputFirstName = input("(Look up profile)\nEnter the first-name associated with profile...\n")
    userInputField = input("\nEnter a field...\n(ex: lastName, number, likes)\n")
    results = look_up_profile(userInputFirstName, userInputField)
    print(f"\nResult(s) for \"{userInputField}\":\n{results}")

if __name__ == "__main__":
    main()