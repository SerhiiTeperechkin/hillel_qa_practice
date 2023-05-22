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
    # [FIXED] Согласно заданию, эти данные необходимо сокрыть от других классов и обеспечить их валидацию:
    # имя не содержит цифр, дата рождения не содержит букв как и номер телефона.
    def __init__(self, name, phone, surname=None, date_of_birth=None):
        self._name = self._validate_name(name)
        self._surname = surname
        self._phone = self._validate_phone(phone)
        self._date_of_birth = self._validate_date_of_birth(date_of_birth)

    def _validate_name(self, name):
        if any(char.isdigit() for char in name):
            raise ValueError("Name cannot contain digits.")
        return name

    def _validate_phone(self, phone):
        if any(char.isalpha() for char in phone):
            raise ValueError("Phone number cannot contain letters.")
        return phone

    def _validate_date_of_birth(self, date_of_birth):
        if date_of_birth is not None and any(char.isalpha() for char in date_of_birth):
            raise ValueError("Date of birth cannot contain letters.")
        return date_of_birth

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def phone(self):
        return self._phone

    @property
    def date_of_birth(self):
        return self._date_of_birth


class Directory:
    def __init__(self):
        self._records = [Record('Police', '102'), Record('Ambulance', '103'), Record('Fire department', '101')]

    def add_record(self, record):
        self._records.append(record)

    def remove_record(self, record):
        if record in self._records:
            self._records.remove(record)
        else:
            raise ValueError("Record not found in the directory.")

    def edit_record(self, record, new_name, new_surname, new_phone, new_date_of_birth):
        if record in self._records:
            record._name = new_name
            record._surname = new_surname
            record._phone = new_phone
            record._date_of_birth = new_date_of_birth

    def get_all_records(self):
        return self._records


class Interface:
    def __init__(self, directory):
        self._directory = directory

    def display_menu(self):
        print("1. Add a record")
        print("2. Remove a record")
        print("3. Edit a record")
        print("4. Display all records")
        print("5. Exit")

    def add_record(self):
        name = input("Enter the name: ")
        surname = input("Enter the surname (optional): ")
        phone = input("Enter the phone number: ")
        date_of_birth = input("Enter the date of birth (optional): ")
        record = Record(name, phone, surname, date_of_birth)
        self._directory.add_record(record)
        print("Record added successfully.")

    def remove_record(self):
        search_query = input("Enter the name or phone number to search for a record: ")
        records = self._search_records(search_query)
        if len(records) == 0:
            print("Record not found.")
            return
        if len(records) == 1:
            self._directory.remove_record(records[0])
            print("Record removed successfully.")
        else:
            print("Multiple records found. Please provide more specific search criteria.")

    # [FIXED] Плохая идея предлагать юзеру ввести индекс записи в списке и перезаписать новой записью.
    # Лучше добавить поиск по имени или номеру и редактировать конкретный атрибут записи,
    # чем заставлять юзера вводить данные по новой целиком. Представь чтоб телефонная
    # книга в смартфоне реально так работала.
    def edit_record(self):
        search_query = input("Enter the name or phone number to search for a record: ")
        records = self._search_records(search_query)
        if len(records) == 0:
            print("Record not found.")
            return
        if len(records) == 1:
            record = records[0]
            attribute = self._select_attribute()
            new_value = input("Enter the new value: ")
            self._update_attribute(record, attribute, new_value)
            print("Record edited successfully.")
        else:
            print("Multiple records found. Please provide more specific search criteria.")

    def _search_records(self, search_query):
        search_query = search_query.lower()
        records = self._directory.get_all_records()
        return [record for record in records if
                search_query in record.name.lower() or search_query in record.phone]

    def _select_attribute(self):
        print("Select the attribute to edit:")
        print("1. Name")
        print("2. Surname")
        print("3. Phone")
        print("4. Date of Birth")
        choice = input("Enter your choice: ")
        if choice == "1":
            return "name"
        elif choice == "2":
            return "surname"
        elif choice == "3":
            return "phone"
        elif choice == "4":
            return "date_of_birth"
        else:
            print("Invalid choice. Attribute not selected.")

    def _update_attribute(self, record, attribute, new_value):
        if attribute == "name":
            record._name = self._validate_name(new_value)
        elif attribute == "surname":
            record._surname = new_value
        elif attribute == "phone":
            record._phone = self._validate_phone(new_value)
        elif attribute == "date_of_birth":
            record._date_of_birth = self._validate_date_of_birth(new_value)

    def display_records(self):
        records = self._directory.get_all_records()
        if len(records) > 0:
            print("Records:")
            for record in records:
                print("Name:", record.name)
                print("Surname:", record.surname)
                print("Phone:", record.phone)
                print("Date of Birth:", record.date_of_birth)
                print("----------------------")
        else:
            print("No records found.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_record()
            elif choice == "2":
                self.remove_record()
            elif choice == "3":
                self.edit_record()
            elif choice == "4":
                self.display_records()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    directory = Directory()
    interface = Interface(directory)
    interface.run()


if __name__ == "__main__":
    main()

