import requests
import json


def get_swapi_data(url):
    response = requests.get(url)
    data = response.json()
    return data


def main(data):
    starships_data = get_swapi_data(data)

    if starships_data['count'] == 0:
        print("No information found on the Millennium Falcon ship")
    else:
        starship_info = starships_data['results'][0]
        starship_pilots_urls = starship_info['pilots']

        pilots_data = []
        for pilot_url in starship_pilots_urls:
            pilot_data = get_swapi_data(pilot_url)
            pilots_data.append(pilot_data)

        starship_info_formatted = {
            'Name': starship_info['name'],
            'Max Speed': starship_info['max_atmosphering_speed'],
            'Class': starship_info['starship_class'],
            'Pilots list': []
        }

        for pilot in pilots_data:
            pilot_info = {
                'Name': pilot['name'],
                'Height': pilot['height'],
                'Weight': pilot['mass'],
                'Home Planet': pilot['homeworld'],
                'Link to Home Planet': pilot['homeworld']
            }
            starship_info_formatted['Pilots list'].append(pilot_info)

        print(json.dumps(starship_info_formatted, indent=4))

        with open('millennium_falcon_info.json', 'w', encoding='utf-8') as file:
            json.dump(starship_info_formatted, file, indent=4)


if __name__ == '__main__':

    starship_url = "https://swapi.dev/api/starships/?search=Millennium%20Falcon"
    main(starship_url)
