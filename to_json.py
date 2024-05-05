import json
import sys

def transform_to_json(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]

    json_object = json.dumps(lines)

    return json_object

if len(sys.argv) <= 1:
    print("Usage: python3 to_json.py <file>")

file_path = sys.argv[1]
json_data = transform_to_json(file_path)
print(json_data)
