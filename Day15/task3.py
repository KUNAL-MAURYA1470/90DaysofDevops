import yaml 
import json

# Open YAML file and read its contents
with open('services.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Convert YAML to JSON
json_data = json.dumps(yaml_data)

# Print the JSON data
print("output:\n",json_data)