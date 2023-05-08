# 3. Написать три класса:
#
# 3.1 класс Справочник(Записная книга, Телефонная книга), описывающий взаимодействие с телефонным справочником.
# Объект этого класса аггрегирует в себе объекты другого класса - Запись(множество записей)
#
# 3.2 класс Запись(Абонент), хранящий такие данные: Имя, Фамилия(необязательно), Телефон,
# Дата рождения(необязательно). Обеспечить валидацию данных и запрет на изменение этих данных другим классом
#
# 3.3 класс Интерфейс, которые обеспечивает взаимодействие с пользователем,
# который вводит данные в терминал. Обеспечить защиту от неверного ввода
#
# 3.4 В функции __main__() написать точку входа и выхода их программы(для ввода пользователя).
#
# Данная программа должна обеспечить: добавление, удаление, редактирование записей с терминала.
# По умолчание в справочнике есть номера экстренных служб, которые нельзя удалить
# или изменить(ни юзеру, ни другому программисту).

class Record:
    def __init__(self, name, phone, surname='', birth_date=''):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.birth_date = birth_date

    def __str__(self):
        return f'{self.name} {self.surname} {self.phone} {self.birth_date}'

    def __repr__(self):
        return str(self)


class Directory:
    def __init__(self):
        self.records = [Record('Police', '102'), Record('Ambulance', '103'), Record('Fire department', '101')]

    def add_record(self, name, phone, surname='', birth_date=''):
        self.records.append(Record(name, phone, surname, birth_date))

    def remove_record(self, index):
        if index > 2 and index < len(self.records):
            self.records.pop(index)
        else:
            print('Cannot remove emergency services')

    def edit_record(self, index, name, phone, surname='', birth_date=''):
        if index > 2 and index < len(self.records):
            self.records[index] = Record(name, phone, surname, birth_date)
        else:
            print('Cannot edit emergency services')

    def __str__(self):
        return '\n'.join([str(record) for record in self.records])


class Interface:
    @staticmethod
    def get_int_input(message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print('Invalid input. Please enter an integer')

    @staticmethod
    def get_string_input(message):
        return input(message)

    @staticmethod
    def get_record_input():
        name = Interface.get_string_input('Enter name: ')
        surname = Interface.get_string_input('Enter surname: ')
        phone = Interface.get_string_input('Enter phone: ')
        birth_date = Interface.get_string_input('Enter birth date (optional): ')
        return name, phone, surname, birth_date

    def __init__(self, directory):
        self.directory = directory

    def run(self):
        while True:
            print('\nDirectory menu')
            print('1. View directory')
            print('2. Add record')
            print('3. Remove record')
            print('4. Edit record')
            print('5. Exit')
            choice = self.get_int_input('Enter your choice: ')

            if choice == 1:
                print(self.directory)
            elif choice == 2:
                name, phone, surname, birth_date = self.get_record_input()
                self.directory.add_record(name, phone, surname, birth_date)
            elif choice == 3:
                index = self.get_int_input('Enter record index: ')
                self.directory.remove_record(index)
            elif choice == 4:
                index = self.get_int_input('Enter record index: ')
                name, phone, surname, birth_date = self.get_record_input()
                self.directory.edit_record(index, name, phone, surname, birth_date)
            elif choice == 5:
                break
            else:
                print('Invalid choice')


def main():
    directory = Directory()
    interface = Interface(directory)
    interface.run()


if __name__ == '__main__':
    main()
