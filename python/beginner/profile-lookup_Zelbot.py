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
    for dict_ in contacts:
        if name in dict_.values():
            if field in dict_:
                return dict_[field]
            return "No such property"
    return "No such contact"


print(look_up_profile("Akira", "likes"))
print(look_up_profile("Kristian", "dislikes"))
print(look_up_profile("Sharon", "lastName"))
