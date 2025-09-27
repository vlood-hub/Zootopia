import json
import requests


def load_data(name):
    """ Loads a JSON file """
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'NA7s7aSou385tD7Cj00X3Q==egXY7wlFAL2Pi1So'})
    return json.loads(response.text)


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


def ask_skin_type(animals_data):
    """ Returns skin type chosen by user """
    skin_types = sorted(set([animal_data['characteristics']['skin_type']
                             for animal_data in animals_data]))
    print("Available skin types:")
    print("\n".join(f"- {item}" for item in skin_types))

    while True:
        skin_type = input("\nChoose one: ")
        if skin_type.capitalize() in skin_types:
            return skin_type
        else:
            print("Please enter a skin type from the list")


def main():
    """ Works with input data and modifies the loaded html files """
    animal = input("Enter an animal you're searching for: ")
    animals_data = load_data(animal)

    orig_html_file = read_write_file('animals_template.html', 'read')
    write_new_html_file = 'animals.html'

    if any(animal_data["name"] == animal.capitalize() for animal_data in animals_data):
        print(animal)
        skin_type_by_user = ask_skin_type(animals_data)

        output = ''
        for animal_data in animals_data:
            if animal_data['characteristics']['skin_type'] == skin_type_by_user.capitalize():
                output += serialize_animal(animal_data)

        print(f"Website was successfully generated to the file {write_new_html_file}")

    else:
        output = f'<h2>The animal <span style="color: red">{animal} </span> doesn\'t exist.</h2>'

    new_html_file = orig_html_file.replace('__REPLACE_ANIMALS_INFO__', output)
    read_write_file(write_new_html_file, 'write', new_html_file)


if __name__ == '__main__':
    main()