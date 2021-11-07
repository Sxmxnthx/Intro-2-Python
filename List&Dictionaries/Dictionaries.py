# Dictionary: Stores a colleciton of labelled items. Each item has a key and a value

person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}

# Values in a dictionary are accessed using their keys

person = {
    'name': 'Jessica',
    'age': 23,
    'height': 172
}
print(person['name'])

print(person['age'])

print(person['height'])

# Exercise 4.5: Print the values of name , post_code and street_number from the dictionary

place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}
print(place['name'])
loc = place['location']
print(place['location':'longitude'])
loc('latitude')

print(place['name'])
print(place['post_code'])
print(place['street_number'])

import random
colours = ['red', 'green', 'blue']
chosen_colour = random.choice(colours)
print(chosen_colour)

firstname = ['joe', 'jack', 'james']
lastname = ['smith','jones','jackson']

firstname = random.choice(firstname)
lastname = random.choice(lastname)
