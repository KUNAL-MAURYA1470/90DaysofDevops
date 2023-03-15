import json

# create a dictionary
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# open a file in write mode and write the dictionary to it as JSON
with open("data.json", "w") as f:
    json.dump(data, f)
    