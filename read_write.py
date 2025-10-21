import csv
import os
from tabulate import tabulate


def tabulate_output(list_out: list[list], header: list) -> print:
    """
    Печатает данные в терминал
    """
    return print(
        tabulate(
            list_out,
            headers=header,
            tablefmt="grid",
            numalign="right",
            showindex=(range(1, (len(list_out) + 1))),
        )
    )


def read_csv(file_name: str) -> list[list]:
    """
    Читает данные из CSV-файла
    """
    result = []
    # Если файл есть в текущей директории
    if os.path.isfile(f".\\{file_name}") | os.path.isfile(file_name):
        with open(file_name, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            # Пропускаем заголовок
            next(reader)

            for row in reader:
                # Приводим строки к числам и добавляем списки в общий список
                row[2] = int(row[2])
                row[3] = float(row[3])
                result.append(row)
    else:
        # Если файла нет
        print(
            f"\nФайл {file_name} не найден в указанной или текущей папке или название файла введено некорректно!\n"
        )
    return result


def write_csv(outfile: str, result: list[list], header: list) -> print:
    """
    Записывает данные в новый CSV-файл
    """
    with open(outfile, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(result)
    return print(f"\nВсе доступные файлы обработаны\n")
