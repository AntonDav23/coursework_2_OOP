![Skypro](https://static.tildacdn.com/tild3364-3965-4237-b664-363533643431/Group_1321317003.svg)

**COURSEWORK_2** — Aircraft Tracker

Описание проекта

Программа для получения и обработки информации о воздушных судах с использованием API OpenStreetMap (Nominatim) и OpenSky Network.

Программа определяет географические границы выбранной страны, получает информацию о находящихся в этой области воздушных судах, преобразует полученные данные в объекты Python и сохраняет результат в JSON-файл.

Функциональность

* Получение географических границ страны через Nominatim API.
* Получение данных о воздушных судах через OpenSky API.
* Преобразование данных API в объекты класса Aeroplane.
* Сортировка самолётов по высоте полёта.
* Получение заданного количества самолётов с наибольшей высотой.
* Фильтрация воздушных судов по стране регистрации.
* Сравнение объектов самолётов по скорости и высоте.
* Сохранение результатов в JSON-файл.

Структура проекта  
├── src/  
│   ├── __init__.py  
│   ├── aeroplane.py  
│   ├── api.py  
│   ├── base_api.py  
│   ├── base_saver.py  
│   ├── json_saver.py  
│   ├── utils.py  
│   └── aircraft.json  
│
├── tests/  
│   ├── test_aeroplane.py  
│   ├── test_api.py  
│   ├── test_base_api.py  
│   ├── test_base_saver.py  
│   ├── test_json_saver.py  
│   └── test_utils.py  
│
├── main.py  
├── pyproject.toml  
├── poetry.lock  
├── .gitignore  
└── README.md  


Запустить программу: poetry run python main.py

Результат работы программы сохраняется в JSON-файл.

Тестирование

Для запуска всех тестов: poetry run pytest  


## Лицензия.
Этот проект распространяется под лицензией MIT.  

<p style="text-align: center;">Developed with ❤️ by A.Davydov</p>

