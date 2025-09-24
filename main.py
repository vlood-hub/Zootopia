import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_write_file(file_path, attr, obj=''):
    """ Read and writes html files """
    if attr == 'read':
        with open(file_path, "r", encoding="utf8") as file_in:
            orig_html_file = file_in.read()
            return orig_html_file
    elif attr == 'write':
        with open(file_path, "w", encoding="utf8") as file_out:
            file_out.write(obj)


def serialize_animal(animal_data):
    """ Serializes animal data """
    output = ''
    output += '<li class="cards__item">'
    output += f'<div class="card__title"> {animal_data["name"]}</div>'
    output += '<div class="card__text">'
    output += '<ul style="list-style-type: square">'
    output += f'''<li style="color: blue"><strong>Scientific name:</strong>
                    {animal_data['taxonomy']['scientific_name']}</li>'''
    output += f'<li><strong>Diet:</strong> {animal_data['characteristics']['diet']}</li>'
    output += f'<li><strong>Location:</strong> {animal_data['locations'][0]}</li>'
    try:
        output += f'<li><strong>Type:</strong> {animal_data['characteristics']['type']}</li>'
        output += f'<li><strong>Group:</strong> {animal_data['characteristics']['group']}</li>'
    except KeyError:
        print()
    output += '</ul>'
    output += '</div>'
    output += '</li>'

    return output


def main():
    """ Works with input data and modifies the loaded html files """
    animals_data = load_data('animals_data.json')

    orig_html_file = read_write_file('animals_template.html', 'read')

    output = ''
    for animal_data in animals_data:
        output += serialize_animal(animal_data)

    new_html_file = orig_html_file.replace('__REPLACE_ANIMALS_INFO__', output)
    read_write_file('animals.html', 'write', new_html_file)


if __name__ == '__main__':
    main()