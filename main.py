import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

with open("animals_template.html", "r", encoding="utf8") as filein:
   html_file = filein.read()

output = ''
for animal_data in animals_data:
    output += f"Name: {animal_data['name']}\n"
    output += f"Diet: {animal_data['characteristics']['diet']}\n"
    output += f"Location: {animal_data['locations'][0]}\n"
    try:
        output += f"{animal_data['characteristics']['type']}\n"
    except KeyError:
       print()
       continue

new_html_file = html_file.replace('__REPLACE_ANIMALS_INFO__', output)
with open("animals.html", "w", encoding="utf8") as fileout:
    fileout.write(new_html_file)