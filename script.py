import argparse


def my_script(*args):
    """
    Скрипт с настройками
    """
    parser = argparse.ArgumentParser(description="Скрипт для обработки csv-файлов")
    parser.add_argument(
        "-f",
        "--files",
        type=str,
        required=True,
        nargs="+",
        help="Введите названия файлов для обработки (для текущей папки) и/или полные пути к файлам",
    )
    parser.add_argument(
        "-r",
        "--report",
        type=str,
        required=True,
        nargs=1,
        help="Введите команду",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        nargs=1,
        help="Введите название отчета",
        default="",
    )

    return parser.parse_args(*args)
