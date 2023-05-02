# 4.Напишіть функцію change_list, яка приймає список і змінює місця його перший і
# останній елемент. У вихідному списку щонайменше 2 елементи.

def change_list(list_for_change):
    if len(list_for_change) < 2:
        return 'В списке меньше 2 элементов'
    else:
        list_for_change[0], list_for_change[-1] = list_for_change[-1], list_for_change[0]
        return list_for_change
