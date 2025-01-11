# dictionary-operations-example
This repository demonstrates basic Python operations using dictionaries. The code provides an example of working with a dictionary containing nested structures and performing key operations such as printing key-value pairs, accessing nested data, and determining the dictionary's length.

## Features
The script performs the following operations:

Print all key-value pairs in the dictionary
Iterates through the dictionary and displays each key with its corresponding value.

Print the salary information
Accesses and prints the salary value from the dictionary.

Print the length of the dictionary
Calculates and prints the total number of top-level keys in the dictionary.

Print the address information
Accesses and prints the nested address dictionary.

Print the street name from the address
Retrieves and prints the street value from the nested address dictionary.

## Sample Dictionary
python
Copy code
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
Getting Started
Prerequisites
Python 3.x installed on your system.
Running the Script
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/dictionary-operations-example.git
cd dictionary-operations-example
Run the Python script:
bash
Copy code
python script.py
Expected Output
css
Copy code
name: John
surname: Doe
age: 78
address: {'street': '123 Main St', 'city': 'New York', 'state': 'NY', 'zipcode': '10001'}
phone: {'home': '123-456-7890', 'work': '987-654-3210'}
email: {'personal': '2t9yD@example.com'}
salary: £1000000
8
{'street': '123 Main St', 'city': 'New York', 'state': 'NY', 'zipcode': '10001'}
123 Main St
Contributing
Contributions, issues, and feature requests are welcome! Feel free to check out the issues page to get started.

## License
This project is licensed under the MIT License. See the LICENSE file for details.