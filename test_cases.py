TEST_MY_SCRIPT_TRUE = [
    (
        "-f products1.csv products2.csv -r average_rating",
        (["products1.csv", "products2.csv"], ["average_rating"], ""),
    ),
    (
        "-f products4.csv products3.csv -r average_rating",
        (["products4.csv", "products3.csv"], ["average_rating"], ""),
    ),
    (
        "-f products1.csv products2.csv -r average_rating -o result",
        (["products1.csv", "products2.csv"], ["average_rating"], ["result"]),
    ),
    (
        "--files products1.csv products2.csv --report average_rating",
        (["products1.csv", "products2.csv"], ["average_rating"], ""),
    ),
    (
        "--files products1.csv products2.csv -r average_rating",
        (["products1.csv", "products2.csv"], ["average_rating"], ""),
    ),
    (
        "-f products3.csv products7.csv --report average_rating",
        (["products3.csv", "products7.csv"], ["average_rating"], ""),
    ),
    (
        "-f products3.csv products7.csv --report average_rating --output answer",
        (["products3.csv", "products7.csv"], ["average_rating"], ["answer"]),
    ),
    (
        "-f C:\\Users\\admin\\Desktop\\test\\products1.csv products2.csv -r average_rating -o answer",
        (
            ["C:UsersadminDesktoptestproducts1.csv", "products2.csv"],
            ["average_rating"],
            ["answer"],
        ),
    ),
]

TEST_MY_SCRIPT_FALSE = [
    (
        "-f products1.csv products2.csv -r average_rating",
        (["products1.csv", "products2.csv"], [" average_rating"], ""),
    ),
    (
        "-f products4.csv products3.csv -r average_rating",
        (["products1.csv", "products3.csv"], ["average_rating"], ""),
    ),
    (
        "-f products1.csv products2.csv -r average_rating -o result",
        (["products1.csv", "products2.csv"], ["average_rating"], ["answer"]),
    ),
    (
        "--files products1.csv products2.csv --report average_rating",
        (["products1.csv", "products2.csv"], ["average"], ""),
    ),
    (
        "--files products1.csv products2.csv -r average_rating",
        (["products1", "products2.csv"], ["average_rating"], ""),
    ),
    (
        "-f products3.csv products7.csv --report average_rating",
        (["products3.csv", "products7.csv"], ["rating"], ""),
    ),
    (
        "-f products3.csv products7.csv --report average_rating --output answer",
        (["products3.csv", "products7.csv"], ["average_rating"], ["result"]),
    ),
    (
        "-f C:\\Users\\admin\\Desktop\\test\\products1.csv products2.csv -r average_rating -o answer",
        (
            ["C:\\Users\\admin\\Desktop\\test\\products1.csv", "products2.csv"],
            ["average_rating"],
            ["answer"],
        ),
    ),
]

TEST_AVERAGE_RATING_TRUE = [
    (
        [
            ["iphone 15 pro", "apple", 999, 4.9],
            ["galaxy s23 ultra", "samsung", 1199, 4.8],
            ["redmi note 12", "xiaomi", 199, 4.6],
            ["iphone 14", "apple", 799, 4.7],
            ["galaxy a54", "samsung", 349, 4.2],
            ["poco x5 pro", "xiaomi", 299, 4.4],
            ["iphone se", "apple", 429, 4.1],
            ["galaxy z flip 5", "samsung", 999, 4.6],
            ["redmi 10c", "xiaomi", 149, 4.1],
            ["iphone 13 mini", "apple", 599, 4.5],
        ],
        ["name", "brand", "price", "rating"],
        ([("apple", 4.55), ("samsung", 4.53), ("xiaomi", 4.37)], ["brand", "rating"]),
    ),
    (
        [
            ["iphone 15 pro", "apple", 999, 4.9],
            ["galaxy s23 ultra", "samsung", 1199, 4.8],
            ["redmi note 12", "xiaomi", 199, 4.6],
            ["iphone 14", "apple", 799, 4.7],
            ["galaxy a54", "samsung", 349, 4.2],
        ],
        ["name", "brand", "price", "rating"],
        ([("apple", 4.8), ("xiaomi", 4.6), ("samsung", 4.5)], ["brand", "rating"]),
    ),
    (
        [
            ["poco x5 pro", "xiaomi", 299, 4.4],
            ["iphone se", "apple", 429, 4.1],
            ["galaxy z flip 5", "samsung", 999, 4.6],
            ["redmi 10c", "xiaomi", 149, 4.1],
            ["iphone 13 mini", "apple", 599, 4.5],
        ],
        ["name", "brand", "price", "rating"],
        ([("samsung", 4.6), ("apple", 4.3), ("xiaomi", 4.25)], ["brand", "rating"]),
    ),
    (
        [],
        ["name", "brand", "price", "rating"],
        ([], ["brand", "rating"]),
    ),  # Пустые данные
]

TEST_AVERAGE_RATING_FALSE = [
    (
        [
            ["iphone 15 pro", "apple", 999, 4.9],
            ["galaxy s23 ultra", "samsung", 1199, 4.8],
            ["redmi note 12", "xiaomi", 199, 4.6],
            ["iphone 14", "apple", 799, 4.7],
            ["galaxy a54", "samsung", 349, 4.2],
            ["poco x5 pro", "xiaomi", 299, 4.4],
            ["iphone se", "apple", 429, 4.1],
            ["galaxy z flip 5", "samsung", 999, 4.6],
            ["redmi 10c", "xiaomi", 149, 4.1],
            ["iphone 13 mini", "apple", 599, 4.5],
        ],
        ["name", "brand", "price", "rating"],
        ([("apple", 4.8), ("xiaomi", 4.6), ("samsung", 4.5)], ["brand", "rating"]),
    ),
    (
        [
            ["iphone 15 pro", "apple", 999, 4.9],
            ["galaxy s23 ultra", "samsung", 1199, 4.8],
            ["redmi note 12", "xiaomi", 199, 4.6],
            ["iphone 14", "apple", 799, 4.7],
            ["galaxy a54", "samsung", 349, 4.2],
            ["poco x5 pro", "xiaomi", 299, 4.4],
            ["iphone se", "apple", 429, 4.1],
            ["galaxy z flip 5", "samsung", 999, 4.6],
            ["redmi 10c", "xiaomi", 149, 4.1],
            ["iphone 13 mini", "apple", 599, 4.5],
        ],
        ["name", "brand", "price", "rating"],
        ([("apple", 4.55), ("samsung", 4.53), ("xiaomi", 4.37)], ["brand", "price"]),
    ),
    (
        [
            ["iphone 15 pro", "apple", 999, 4.9],
            ["galaxy s23 ultra", "samsung", 1199, 4.8],
            ["redmi note 12", "xiaomi", 199, 4.6],
            ["iphone 14", "apple", 799, 4.7],
            ["galaxy a54", "samsung", 349, 4.2],
        ],
        ["name", "brand", "price", "rating"],
        ([("samsung", 4.6), ("apple", 4.3), ("xiaomi", 4.25)], ["brand", "rating"]),
    ),
    (
        [
            ["poco x5 pro", "xiaomi", 299, 4.4],
            ["iphone se", "apple", 429, 4.1],
            ["galaxy z flip 5", "samsung", 999, 4.6],
            ["redmi 10c", "xiaomi", 149, 4.1],
            ["iphone 13 mini", "apple", 599, 4.5],
        ],
        ["name", "brand", "price", "rating"],
        ([("apple", 4.55), ("samsung", 4.53), ("xiaomi", 4.37)], ["brand", "rating"]),
    ),
    (
        [],
        ["name", "brand", "price", "rating"],
        [
            ([("samsung", 4.6), ("apple", 4.3), ("xiaomi", 4.25)], ["brand", "rating"]),
        ],
    ),  # Пустые данные
]

TEST_READ_CSV_TRUE = [
    (
        "products1.csv",
        [
            ["iphone 15 pro", "apple", 999, 4.9],
            ["galaxy s23 ultra", "samsung", 1199, 4.8],
            ["redmi note 12", "xiaomi", 199, 4.6],
            ["iphone 14", "apple", 799, 4.7],
            ["galaxy a54", "samsung", 349, 4.2],
        ],
    ),
    (
        "products2.csv",
        [
            ["poco x5 pro", "xiaomi", 299, 4.4],
            ["iphone se", "apple", 429, 4.1],
            ["galaxy z flip 5", "samsung", 999, 4.6],
            ["redmi 10c", "xiaomi", 149, 4.1],
            ["iphone 13 mini", "apple", 599, 4.5],
        ],
    ),
    ("C:\\Users\\admin\\Desktop\\test\\products1.csv", []),  # Неверный путь к файлу
    ("products3.csv", []),  # Неверное название файла
    ("", []),  # Пустые данные
]

TEST_READ_CSV_FALSE = [
    (
        "products1.csv",
        [
            ["poco x5 pro", "xiaomi", 299, 4.4],
            ["iphone se", "apple", 429, 4.1],
            ["galaxy z flip 5", "samsung", 999, 4.6],
            ["redmi 10c", "xiaomi", 149, 4.1],
            ["iphone 13 mini", "apple", 599, 4.5],
        ],
    ),
    (
        "products2.csv",
        [
            ["iphone 15 pro", "apple", 999, 4.9],
            ["galaxy s23 ultra", "samsung", 1199, 4.8],
            ["redmi note 12", "xiaomi", 199, 4.6],
            ["iphone 14", "apple", 799, 4.7],
            ["galaxy a54", "samsung", 349, 4.2],
        ],
    ),
    (
        "C:\\Users\\admin\\Desktop\\test\\products1.csv",
        [
            ["galaxy a54", "samsung", 349, 4.2],
        ],
    ),  # Неверный путь к файлу
    (
        "products3.csv",
        [
            ["galaxy a54", "samsung", 349, 4.2],
        ],
    ),  # Неверное название файла
    (
        "",
        [
            ["galaxy a54", "samsung", 349, 4.2],
        ],
    ),  # Пустые данные
]
