import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for i in range(len(animals_data)):
    print(f"Name {animals_data[i]['name']}")
    print(f"Diet: {animals_data[i]['characteristics']['diet']}")
    print(f"Location: {animals_data[i]['locations'][0]}")
    try:
        print(f"Type: {animals_data[i]['characteristics']['type']}\n")
    except KeyError:
       print()
       continue

