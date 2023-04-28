# 1. Створити проект на github, "залити" на віддалений репозиторій всі свої ДЗ до 5-ї лекції
print('Задание №1\n')

print('This is my git_repo: https://github.com/SerhiiTeperechkin/hillel_qa_practice')

# 2. Створити реалізацію квадратного рівняння a•x²+b•x+c=0(користувач вводить a, b, c),
# якщо дискримінант від'ємний викликати виняток DiscriminantError і вивести відповідне повідомлення.
print('\nЗадание №2\n')


class DiscriminantError(Exception):
    pass


a, b, c = [float(input(f'Введите значение коэффициента {coefficient}: ')) for coefficient in ('a', 'b', 'c')]

try:
    disc = b * b - 4 * a * c

    if disc < 0:
        raise DiscriminantError

    root = (disc ** 0.5)
    x_1 = (-b + root) / (2 * a)
    if disc != 0:
        x_2 = (-b - root) / (2 * a)
        print(f'Решения {x_1} и {x_2}')
    else:
        print(f'Единственным решением является x = {x_1}')
except DiscriminantError:
    print(f'Уравнение не имеет решений т.к. дискриминант меньше нуля')

# 3. Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу,
# що складається з числа, оператора (як мінімум + і -) та іншого числа,
# розділених пробілом (наприклад, 1 + 1). Використовуйте str.split()
# a. Якщо вхідні дані не складаються з трьох елементів, генеруйте ексепшн FormulaError.
# b. Спробуйте перетворити перший і третій елемент на float ( float_value = float(str_value)).
# Спіймайте будь-яку ValueError і згенеруйте замість нього FormulaError
# c. Якщо другий елемент не є «+» або «-», киньте ексепшн FormulaError
print('\nЗадание №3\n')


class FormulaError(Exception):
    pass


inp = input('Введит формулу типа "2 + 2": ')
try:
    try:
        if len(inp.split(' ')) > 3:
            raise FormulaError('Введено более чем 3 элемнта')

        num1 = float(inp.split(' ')[0])
        num2 = float(inp.split(' ')[2])
        operation = inp.split(' ')[1]

        if operation == '+':
            print(num1 + num2)
        elif operation == '-':
            print(num1 - num2)
        else:
            raise FormulaError('Введен неподдерживаемый оператор вычисления')

    except ValueError:
        raise FormulaError('Введены неверные значения')
except FormulaError as error:
    print(error)
