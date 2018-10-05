"""
My solution for: https://github.com/the-vampiire/hacktoberithms/issues/2
"""

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

def profile_lookup(name, field):
    for contact in contacts:
        if name == contact["firstName"]:
            return contact.get(field, "No such property")
    return "No such contact"


print(profile_lookup("Kristian", "likes"))
