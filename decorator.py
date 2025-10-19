import csv
import os
from tabulate import tabulate


def csv_decorator(func):
    """
    Декоратор для чтения csv-файлов и записи обработанной информации в новый csv-файл
    """

    def wrapper(input_filenames: list, outfile: str = "") -> csv:
        """
        Функция для обработки CSV-файлов:
        - Читает данные из входных файлов
        - Обрабатывает данные
        - Выводит таблицу в терминал
        - Записывает обработанные данные в новый CSV-файл
        """
        # Общий список для всех файлов
        lines = []
        # Обрабатываем все полученные файлы csv
        for file in input_filenames:
            # Если файл есть в текущей директории
            if os.path.isfile(f".\\{file}") | os.path.isfile(file):
                with open(file, "r", newline="", encoding="utf-8") as file:
                    # Читаем csv файл
                    reader = csv.reader(file)
                    # Запоминаем заголовок
                    header = next(reader)

                    for row in reader:
                        # Приводим строки к числам и добавляем списки в общий список
                        row[2] = int(row[2])
                        row[3] = float(row[3])
                        lines.append(row)
            elif os.path.isfile(file):
                pass
            else:
                # Если файла нет
                print(f"Файл {file} не найден в указанной или текущей папке")
                continue
        # Если открыли хотя бы один файл
        if lines != []:
            # Открываем файл для записи
            with open(outfile, "a", newline="", encoding="utf-8") as outfile:
                writer = csv.writer(outfile)
                # Записываем заголовок
                writer.writerow(header)

                # Выбранная функция для обработки данных
                result = func(lines)
                # Печать в терминал
                print(
                    tabulate(
                        result, headers=header, tablefmt="grid", showindex="always"
                    )
                )

                # Записываем данные в файл после обработки
                for line in result:
                    writer.writerow(line)
            print("Все доступные файлы обработаны")
        # Если не добавилось ничего, то ни один файл не был открыт
        else:
            print(
                "Ни одного файла не найдено в текущей папке или по указанному пути, запустиите скрипт заново с корректными параметрами"
            )

    return wrapper
