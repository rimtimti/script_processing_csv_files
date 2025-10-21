import functools
from read_write import read_csv, tabulate_output, write_csv


def csv_decorator(func):

    @functools.wraps(func)
    def wrapper(input_filenames: list, outfile: str = ""):
        """
        Основная функция-декоратор для обработки CSV-файлов:
        - Читает данные из входных файлов
        - Обрабатывает данные
        - Выводит таблицу в терминал
        - Записывает обработанные данные в новый CSV-файл
        """
        # Общий список для всех файлов
        lines = []
        # # Заголовок всегда одинаковый
        header = ["name", "brand", "price", "rating"]

        # Обрабатываем все полученные файлы csv
        for file in input_filenames:
            out = read_csv(file)
            lines.extend(out)

        # Выбранная функция для обработки данных
        result, header = func(lines, header)

        # Если открыли хотя бы один файл
        if lines != []:
            # Печать в терминал
            tabulate_output(result, header)
            # Записываем файл csv
            write_csv(outfile, result, header)

        # Если не добавилось ничего, так как ни один файл не был открыт
        else:
            return print(
                f"\nНи одного файла не найдено в текущей папке или по указанному пути, запустите скрипт заново с корректными параметрами\n"
            )

    return wrapper
