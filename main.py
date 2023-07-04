import json  # Java Script Object Notation

pets = {
    'name': 'Charly',
    'age': 15,
    'meals': ['Purina', 'Hills'],
    'owner': {'fname': 'Bill', 'sname': 'Gates'}
}

with open('pets.json', 'w') as pet_file:
    json.dump(pets, pet_file)
