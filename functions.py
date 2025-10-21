from collections import Counter
from decorator import csv_decorator


@csv_decorator
def average_rating(non_sort_list: list[list], header) -> list:
    """
    Сортирует бренды телефонов по среднему рейтингу (округление до сотых) от большего к меньшему
    """
    # Мне не нравится реализация (вероятно, можно компактнее и быстрее), но времени не очень много, главное - работает

    brands = {}
    header = [header[1], header[3]]
    for item in non_sort_list:
        brand, rating = item[1], item[3]
        if brands.get(brand) == None:
            brands[brand] = round(rating, 1)
        else:
            brands[brand] = round(brands.get(brand) + rating, 1)
    counter = dict(Counter(i[1] for i in non_sort_list))
    for i in brands:
        mean = brands.get(i) / counter.get(i)
        brands[i] = round(mean, 2)

    return sorted(brands.items(), key=lambda item: item[1], reverse=True), header
