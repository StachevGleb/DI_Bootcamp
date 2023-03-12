import json
json_file = 'file.json'
with open(json_file) as f:
    family = json.load(f)
print(family)
