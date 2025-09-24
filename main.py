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
    output += f'<div class="card__title"> {animal_data["name"]}<br/></div>'
    output += '<p class="card__text">'
    output += f'<strong>Diet:</strong> Diet: {animal_data['characteristics']['diet']}<br/>'
    output += f'<strong>Location:</strong> {animal_data['locations'][0]}<br/>'
    try:
        output += f'<strong>Type:</strong> {animal_data['characteristics']['type']}<br/>'
        output += '</p>'
        output += '</li>'
    except KeyError:
       print()
       continue

new_html_file = html_file.replace('__REPLACE_ANIMALS_INFO__', output)
with open("animals.html", "w", encoding="utf8") as fileout:
    fileout.write(new_html_file)

    """<li class="cards__item">
  <div class="card__title">Wire Fox Terrier</div>
  <p class="card__text">
      <strong>Diet:</strong> Carnivore<br/>
      <strong>Location:</strong> North-America and Canada<br/>
      <strong>Type:</strong> mamal<br/>
  </p>
</li>"""