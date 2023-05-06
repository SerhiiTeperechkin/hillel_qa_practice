import os
import pickle


# Написать скрипт, который подсчитает количество папок и файлов по заданному пути. Если такого нет,
# то по всей системе(/ - для линукс/мак. Диск С - для виндоус). Для удобства можно установить граничное значение
# числа папок(и/или файлов), после которого скрипт не будет продолжать работу. Среди найденных файлов показать
# самый большой и самый маленький по размеру, а так же с самым длинным и коротким именем. Если во время работы
# скрипт был прерван(KeyboardInterrupt), то промежуточные результаты сериализуются
# в файл и при повторном запуске эти пути исключаются из проверки.


def directories_files_counter(path, processed_paths):
    high_size = None
    lower_size = None
    long_name = None
    short_name = None
    folders_count = 0
    files_count = 0

    for root, dirs, files in os.walk(path):

        if root in processed_paths:
            continue

        folders_count += len(dirs)
        files_count += len(files)

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            if high_size is None or file_size > os.path.getsize(high_size):
                high_size = file_path

            if lower_size is None or file_size < os.path.getsize(lower_size):
                lower_size = file_path

            if long_name is None or len(file) > len(long_name):
                long_name = file

            if short_name is None or len(file) < len(short_name):
                short_name = file

    return folders_count, files_count, high_size, lower_size, long_name, short_name


def process_path_saving(path, processed_paths):
    with open(path, 'wb') as file:
        pickle.dump(processed_paths, file)


def process_path_loading(path):
    if not os.path.exists(path):
        return []

    with open(path, 'rb') as file:
        return pickle.load(file)


def get_result(path, processed_paths_file):
    """
    Get result from directories_files_counter, process_path_loading, process_path_saving functions

    :param path: path to your directory
    :param processed_paths_file: your processed paths file
    :return: the result in a dictionary
    """
    try:
        processed_paths = process_path_loading(processed_paths_file)
        folders, files, high_size, lower_size, long_name, \
            short_name = directories_files_counter(path, processed_paths)

        result_data = {"Folders count": folders,
                       "Files count": files,
                       "Higher size file": {"File name": f"{high_size}",
                                            "File size": f"({os.path.getsize(high_size)} bytes)"},
                       "Lower size file": {"File name": f"{lower_size}",
                                           "File size": f"({os.path.getsize(lower_size)} bytes)"},
                       "Longname file": long_name,
                       "Shortname file": short_name
                       }

        processed_paths.append(path)
        process_path_saving(processed_paths_file, processed_paths)

        return result_data

    except KeyboardInterrupt as ex:
        print("\n[LOG]: Script interrupt. Saving intermediate results", ex)
        processed_paths.append(path)
        process_path_saving(processed_paths_file, processed_paths)
        print("[LOG]: Intermediate results saved")


your_path = r'C:\Users\sereg\PycharmProjects\hillel_qa\lessons 7'
processed_paths_file = 'processed_paths.pkl'
print(get_result(your_path, processed_paths_file))
