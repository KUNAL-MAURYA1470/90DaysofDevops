import json

# create a dictionary
data = {
    "name": "Kunal",
    "age": 20,
    "city": "Surat"
}

# open a file in write mode and write the dictionary to it as JSON
with open("data.json", "w") as f:
    json.dump(data, f)
