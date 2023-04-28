# 1. Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'
print('Задание №1\n')

try:
    word = str(input('Введите слово: '))
    if word == word[::-1]:
        print("+")
    else:
        print("-")
except Exception as ex:
    print(ex)

# 2. Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті,
# вивести 'YES', інакше 'NO'
print('\nЗадание №2\n')

try:
    text = input('Введите текст: ')
    search_word = input('Ввидите слово для поиска в тексте: ')
    if search_word in text:
        print('YES')
    else:
        print('NO')
except Exception as ex:
    print(ex)

# 3. Користувач водить рядок. Якщо він починається на 'abc', замінити їх на 'www',
# інакше додати в кінець рядка 'zzz'.
print('\nЗадание №3\n')

try:
    user_string = input('Введите что-нибудь: ')
    if user_string.startswith('abc'):
        # Если нам нужно удалить все совпадения, то мы запишем: user_string.replace('abc', 'www')
        user_string = user_string.replace('abc', 'www', 1)
        print(user_string)
    else:
        # WAY №1
        str_into_list = list(user_string)
        str_into_list.extend('zzz')
        print(''.join(str_into_list))

        # WAY №2
        # print(f'{user_string}zzz')

        # WAY №3
        # print(user_string.ljust(len(user_string) + 3, 'z'))
except Exception as ex:
    print(ex)

# 4. Написати валідатор для пошти. Користувач вводить пошту, а програма повинна перевірити,
# що в пошті є символ '@' і '.', і якщо це так, вивести "YES", інакше "NO"
print('\nЗадание №4\n')

try:
    email_input = input('Введите ваш e-mail: ')
    if '@' and '.' in email_input:
        print('YES')
    else:
        print('NO')
except Exception as ex:
    print(ex)

# 5. Користувач водить текст через пробіл. Конвертувати текст у список.
# Вивести остані 3 елементи зі списку, якщо список містить менше 3-х елементів,
# вивести повідомлення про те що кількість елементів менша за 3 і вказати
# кількість елементів поточного списку
print('\nЗадание №5\n')

try:
    user_text = input('Введите текст: ')
    text_in_list = []
    for word in user_text.split(' '):
        text_in_list.append(word)
    if len(text_in_list) > 3:
        print(text_in_list[-3:])
    else:
        print(f'Длина списка менешь 3 элемемнтов!\nЭлементов в списке: {len(text_in_list)}')
except Exception as ex:
    print(ex)
