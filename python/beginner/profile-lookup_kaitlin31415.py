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
	value = "No such Contact"
	for contact in contacts:
		first = contact.get("firstName");
		if (first.upper() == name.upper()):
			if(field in contact):
				value = contact[field]
				
			else: 
				value = "No Such Property"
				
	return value 
	
	
	
print(look_up_profile("Akira", "likes"))			

