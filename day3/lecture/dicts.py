# dictionaries store data in key-value pairs
# dictionaries are unordered, changeable and do not allow duplicate keys

# dictionaries are defined by curly brackets
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person) # {'name': 'John', 'age': 30, 'city': 'New York'}

# access items using the key
print(person["name"]) # John
print(person["age"]) # 30
print(person["city"]) # New York

# change item value
person["city"] = "Los Angeles"
print(person) # {'name': 'John', 'age': 30, 'city': 'Los Angeles'}

# add items
person["job"] = "developer"
print(person) # {'name': 'John', 'age': 30, 'city': 'Los Angeles', 'job': 'developer'}

# remove items
person.pop("age")
del person["job"]
print(person) # {'name': 'John', 'city': 'Los Angeles'}

# iterate through a dictionary
for key in person:
    print(key, person[key])
# name John
# city Los Angeles

# you can also use the items() method to get the key-value pairs  (key, value)
for key, value in person.items():
    print(key, value)
# name John
# city Los Angeles

# check if a key exists
print("name" in person) # True
print("age" in person) # False

# get the number of items in a dictionary
print(len(person)) # 2