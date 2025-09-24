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
    output += '<li class="cards__item">'
    output += f"Name: {animal_data['name']}<br/>"
    output += f"Diet: {animal_data['characteristics']['diet']}<br/>"
    output += f"Location: {animal_data['locations'][0]}<br/>"
    try:
        output += f"Type: {animal_data['characteristics']['type']}<br/>"
        output += '</li>'
    except KeyError:
       print()
       continue

new_html_file = html_file.replace('__REPLACE_ANIMALS_INFO__', output)
with open("animals.html", "w", encoding="utf8") as fileout:
    fileout.write(new_html_file)