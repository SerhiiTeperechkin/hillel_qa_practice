# 1. Існує список з іменами ["john", "marta", "james", "amanda", "marianna"], перетворити рядок,
# щоб кожне ім'я явно починалися з великої літери.
print('Задание №1\n')

names_lower = ["john", "marta", "james", "amanda", "marianna"]
names_capitalize = []
for name in names_lower:
    names_capitalize.append(name.capitalize())
print(names_capitalize)

# 2. Є список друзів ["John", "Marta", "James", "Amanda", "Marianna"]. Виведіть імена в консолі,
# кожен з нового рядка, вирівнюючи праву сторону, використовуючи метод рядка та форматування
# через F String. Також над іменами першим рядком виведіть NAME,
# де NAME має бути посередині(string.center()), а решта простору заповнена символом "*"
print('\nЗадание №2\n')

friends_list = ["John", "Marta", "James", "Amanda", "Marianna"]
friends_list_newline = ['NAME'.center(10).replace(' ', '*')]
for friend in friends_list:
    friends_list_newline.append(friend.rjust(10))

for newline_name in friends_list_newline:
    print(f'{newline_name}')

# 3. У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] ,
# перетворити його у список змінних для Пайтона snace_case, "friends_list", "my_tuple"]
print('\nЗадание №3\n')

camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []
for item in camel_case_list:
    snake_case_list.append(
        (''.join(['_' + i.lower() if i.isupper()
                  else i for i in item]).lstrip('_'))
    )
print(snake_case_list)

# 4. Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників
# цих мов (значення). Виведіть по черзі для усіх елементів словника повідомлення типу
# My favorite programming language is Python. It was created by Guido van Rossum..
# Видаліть, на ваш вибір, одну пару «мова: розробник» із словника. Виведіть словник на екран.
print('\nЗадание №4\n')

# Создали словарь типа 'language:author'
language_author = {
    'Python': 'Guido van Rossum',
    'JavaScript': 'Brendan Eich',
    'Java': 'James Gosling',
    'C++': 'Bjarne Stroustrup'
}

for elements in language_author.items():
    print(f'My favorite programming language is {elements[0]}. It was created by {elements[1]} ...')

# Удалил из словаря C++
language_author.pop('C++')
print(language_author)

# 5. Створіть англо-німецький словник, який називається e2g, і виведіть його на екран.
# Слова для словника: stork / storch, hawk / falke, woodpecker / specht і owl / eule.
# Виведіть німецький варіант слова owl. Додайте у словник, на ваш вибір, ще два слова та їхній переклад.
# Виведіть окремо: словник; ключі і значення словника у вигляді списків.
print('\nЗадание №5\n')

e2g = {
    'stork': 'storch',
    'hawk': 'falke',
    'woodpecker': 'specht',
    'owl': 'eule'
}
print(f"eng - owl ; german - {e2g.get('owl')}")
e2g.update({
    'snake': 'schlange',
    'frog': 'frosch'
})

dict_keys = []
dict_values = []

for keys in e2g.keys():
    dict_keys.append(keys)
for values in e2g.values():
    dict_values.append(values)
print(f"Dict: {e2g}\nDict keys: {dict_keys}\nDict values: {dict_values}")

# 6. Створіть багаторівневий словник subjects навчальних предметів.
# Використайте наступні рядки для ключів верхнього рівня: 'science', 'humanities' і 'public'.
# Зробіть так, щоб ключ 'science' був ім’ям іншого словника, який має ключі 'physics', 'computer science'
# і 'biology'. Зробіть так, щоб ключ 'physics' посилався на список рядків зі значеннями 'nuclear physics',
# 'optics' і 'thermodynamics'. Решта ключів повинні посилатися на порожні словники.
# Виведіть на екран ключі subjects['science'] і значення subjects['science']['physics'].
print('\nЗадание №6\n')

subjects = {'science': {'physics': ['nuclear physics', 'optics', 'thermodynamics'],
                        'computer science': {},
                        'biology': {}},
            'humanities': {},
            'public': {}}

subjects_science = []
subjects_science_physics = []
for subject in subjects['science']:
    subjects_science.append(subject)
for subject in subjects['science']['physics']:
    subjects_science_physics.append(subject)
print(f'Keys subjects["science"]: {subjects_science}\n'
      f'Keys subjects["science"]["physics"] : {subjects_science_physics}')


# 7. Напишіть програму, яка виводить словник, в якому ключі є числами від 1 до 15 (обидва включені),
# а значення є квадратами ключів. Генерація ключів та значень має бути виконана через цикл.
print('\nЗадание №7\n')

diction = {}
for i in range(1, 16):
    diction.update({
        i: i**2
    })
print(diction)
