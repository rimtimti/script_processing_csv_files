from collections import Counter
from decorator import csv_decorator


@csv_decorator
def average_rating(non_sort_list: list[list], header) -> list:
    """
    Сортирует бренды телефонов по среднему рейтингу (округление до сотых) от большего к меньшему
    """
    # Мне не нравится реализация (вероятно, можно компактнее и быстрее), но времени не очень много, главное - работает

    header = [header[1], header[3]]
    counter = Counter(i[1] for i in non_sort_list)

    non_sort_list = [{item[:][1]: item[:][3]} for item in non_sort_list]
    result = Counter()
    for i in non_sort_list:
        result.update(i)

    for i in counter:
        mean = result.get(i) / counter.get(i)
        result[i] = round(mean, 2)

    return sorted(result.items(), key=lambda item: item[1], reverse=True), header


# @csv_decorator
# def average_price(non_sort_list: list[list], header) -> list:
#     """
#     Сортирует бренды телефонов по средней цене (округление до сотых) от большего к меньшему
#     """
#     pass
#     header = [header[1], header[2]]
#     counter = Counter(i[1] for i in non_sort_list)

#     non_sort_list = [{item[:][1]: item[:][2]} for item in non_sort_list]
#     result = Counter()
#     for i in non_sort_list:
#         result.update(i)

#     for i in counter:
#         mean = result.get(i) / counter.get(i)
#         result[i] = round(mean, 2)

#     return sorted(result.items(), key=lambda item: item[1], reverse=True), header
