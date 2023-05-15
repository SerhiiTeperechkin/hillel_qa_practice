import json

# Знайти ідентифікатор групи, де знаходиться найбільша кількість жінок, народжених після 1977 року.
# Як відповідь необхідно вказати через пробыл ідентифікатор знайденої групи і скільки в ній було жінок,
# народжених після 1977 року. Файл group_people.json


def max_female_group(path):
    """
    :param path: path to group_people.json
    :return: id_group and how many women were in it, born after 1977
    """
    with open(f'{path}', 'r') as file:
        load = json.load(file)
        max_group_id = None
        max_female = 0

        for group in load:
            id_group = group['id_group']
            female_count = 0

            for data in group['people']:
                if data['gender'] == 'Female' and data['year'] > 1977:
                    female_count += 1

            if female_count > max_female:
                max_group_id = id_group
                max_female = female_count

        return f'ID: {max_group_id}\nFemale count: {max_female}'
