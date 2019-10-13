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
    found = False

    for contact in contacts:
        if name == contact["firstName"]:
            found = True

            if field in contact:
                return contact[field]
            else:
                return "No such property."

    if not found:
        return "No such contact."

if __name__ == "__main__":
        contact_name = input("First name of your contact: ")
        key = input("Field you want to retrieve: ")
        info = look_up_profile(contact_name, key)
        print(info)
