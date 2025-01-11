person = {
    "name": "John",
    "surname": "Doe",
    "age": 78,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zipcode": "10001"
    },
    "phone": {
        "home": "123-456-7890",
        "work": "987-654-3210"
    },
    "email": {
        "personal": "2t9yD@example.com",
    
},
    "salary": "£1000000"
}

# Print all key-value pairs in the dictionary

for key, value in person.items():
    print(f"{key}: {value}")
#Print salary information
print(person["salary"])
#Print the length of the dictionary
print(len(person))
#Print the address information
print(person["address"])
#Print the street name from the address
print(person["address"]["street"])