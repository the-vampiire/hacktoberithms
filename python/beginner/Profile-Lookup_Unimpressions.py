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
];


def look_up_profile(name, field):
    for lookup in contacts:
        lookupname = lookup.get('firstName')
        if lookupname.casefold() == name.casefold():
            lookupfield = lookup.get(field)
            if lookupfield == lookup[field]:
                return lookupfield
            else:
                return "No Such property."
    return "No such contact."

#Change these values to test your function
print(look_up_profile("Akira", "number"))
