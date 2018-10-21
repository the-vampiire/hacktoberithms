# -*- coding: utf-8 -*-


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
    
    for contact in contacts:
        
        if contact["firstName"] == name and contact.get(field) != None:
            return contact[field]
        elif contact.get(field) == None:
            return "No such property"
    return "No such contact"

#Change these values to test your function
print(look_up_profile("Akira", "likes"))