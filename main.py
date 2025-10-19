from functions import average_rating
from script import my_parser


if __name__ == "__main__":
    input_files, report, output = my_parser()
    if output == None:
        output = f"{report[0]}.csv"
    else:
        output = f"{output[0]}.csv"

    match report[0]:
        case "average_rating":
            average_rating(input_files, output)
        # Сюда можно добавлять новые команды, нужно только написать функцию и обернуть в декоратор
        # case "price_rating":
        #     price_rating(input_files, output)
