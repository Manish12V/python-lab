#dictionary

person = { "name": "gautam","age": 19}
print(person)

# Add a new value
person["mobile no"] = "985985985"
print("Dictionary after adding a new value:", person)

# Changing a value 
person["age"] = 21
print("Dictionary after changing a value:", person)

# Get a value from the dictionary
name = person.get("name")
print("Name:", name)


