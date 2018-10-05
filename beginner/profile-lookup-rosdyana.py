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


def look_up_profile(name: str, field: str) -> str:
    """Challenge
    We have a list of dictionaries representing different people in our
    contacts list. Complete the look_up_profile() function that takes
    name and a field as arguments included below. The function should
    check if name is an actual contact's firstName and the given field
    exists in that contact dictionary. If both are true, then return the
    "value" of that field. If name does not correspond to any contacts
    then return "No such contact" If the field does not correspond to
    any valid properties of a contact found to match name then return
    "No such property

    >>> look_up_profile('Sherlock', 'number')
    '0487345643'
    >>> look_up_profile('Notthere', 'likes')
    'No such contact'
    >>> look_up_profile('Akira', 'notthere')
    'No such property'
    """
    result = 'No such contact'
    for contact in contacts:
        first_name = contact.get('firstName')
        if first_name and name.casefold() == first_name.casefold():
            if field in contact:
                return contact[field]
            else:
                result = 'No such property'
    return result


