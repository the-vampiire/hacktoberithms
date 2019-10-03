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
    gen = (index for index, i in enumerate(contacts) if name == i["firstName"])
    try:
        result = contacts[next(gen)]
        if result[field]:
            return result
    except:
        return "No such contact"


print(look_up_profile("Akira", "firstName"))  # True
print(look_up_profile("topkek", "firstName"))  # False
print(look_up_profile("Kristian", "likes"))  # True
print(look_up_profile("Kris", "likes"))  # False
print(look_up_profile("Kris", "lol"))  # False



