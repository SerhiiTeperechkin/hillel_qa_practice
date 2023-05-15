import json

# Знайти найуспішнішого менеджера за підсумковою сумою продажів. Як відповідь потрібно через пробыл
# вказати спершу його ім'я, потім прізвище і після загальну суму його продажів.Файл manager_sales.json


def best_sale_manager(path):
    """
    :param path: path to manager_sales.json
    :return: the best manager first name, then last name and then the total amount of his sales
    """
    with open(f'{path}', 'r') as file:
        load = json.load(file)
        best_manager_first_name = None
        best_manager_last_name = None
        best_manager_total_sale = 0

        for managers in load:
            name = managers['manager']['first_name']
            last_name = managers['manager']['last_name']
            total_sales = 0

            for data in managers['cars']:
                total_sales += data['price']

            if total_sales > best_manager_total_sale:
                best_manager_total_sale = total_sales
                best_manager_first_name = name
                best_manager_last_name = last_name

        return f'Best manager: {best_manager_first_name} {best_manager_last_name}\n' \
               f'Total sales: {best_manager_total_sale}'

