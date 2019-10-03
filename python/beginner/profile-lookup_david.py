"""
Complete the look_up_profile() function that takes name and a field as arguments included below
The function should check if name is an actual contact's firstName and the given field exists in that contact dictionary.
If both are true, then return the "value" of that field.
If name does not correspond to any contacts then return "No such contact"
If the field does not correspond to any valid properties of a contact found to match name then return "No such property"
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


def look_up_profile(name: str, field: str) -> str:
    for contact in contacts:
        first_name = contact.get("firstName")
        if first_name and first_name.casefold() == name.casefold():
            field_value = contact.get(field)
            return field_value if field_value else "No such property"
    return "No such contact"
            


# Change these values to test your function
look_up_profile("Akira", "likes")
