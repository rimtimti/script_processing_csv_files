from functions import average_rating
# from functions import average_price
from script import my_script


def run(*arsg):
    parser = my_script()
    if parser.output == "":
        output = f"{parser.report[0]}.csv"
    else:
        output = f"{parser.output[0].split(".")[0]}.csv"

    match parser.report[0]:
        case "average_rating":
            average_rating(parser.files, output)
        # Сюда можно добавлять новые команды, нужно только написать функцию и обернуть в декоратор,
        # например я добавил новую функцию (закомментировано)

        # case "average_price":
        #     average_price(parser.files, output)


if __name__ == "__main__":
    run()
