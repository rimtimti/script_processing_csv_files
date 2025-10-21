# Cкрипт для обработки csv-файлов

Позволяет делать отчеты из csv-файлов определенного формата (см. примеры: products1.py и products2.py).
Считаем что содержимое файлов всегда валидно, ограничений по памяти нет, всё можно читать в память

## Установка
Откройте среду разработки:
```
например, Visual Studio Code, откройте терминал
```

Скопируйте репозиторий на локальный компьютер:
```
git clone <https or SSH URL>
```

Перейдите в папку проекта:
```
cd <folder>
```

Создайте и активируйте локальное окружение:
```
Для Windows
python -m venv venv
venv\Scripts\activate

Для Linux
python3 -m venv venv
source venv/bin/activate
```

Обновите pip:
```
python -m pip install --upgrade pip
```

Установите зависимости:
```
pip install -r requirements.txt
```

Старт скрипта:
```
python maшт.py -f products1.csv products2.csv -r average_rating -o result
или
python maшт.py --files products1.csv products2.csv --report average_rating --output result
или
python maшт.py -f products1.csv products2.csv -r average_rating
где
products1.csv products2.csv - названия файлов (должны быть в текущей директории) или полные пути к файлам (обязательно)
average_rating - команда для отчета (обязательно)
result - название файла отчета (необязательно)
```
Примеры ответа скрипта в файлах: average_rating.csv и rating.csv
Пример запуска скрипта в файле: screen.png

Для добавления другого отчета нужно:
1. написать новую фунцию в functions.py и обернуть в декоратор (см. готовую функцию)
2. дописать новую команду в функцию run (см. case-пример) в main.py
3. написать тесты для новой функции