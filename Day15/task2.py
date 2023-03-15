import json

# read the services from the JSON file
with open("services.json", "r") as f:
    data = json.load(f)

print("aws:"+ data["services"]["aws"]["name"])
print("azure:"+ data["services"]["azure"]["name"])
print("gcp:"+ data["services"]["gcp"]["name"])

