# 8.1
print("1 задание")
countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Япония": "Токио"
}
print("а) Все страны и их столицы:")
for country, capital in countries.items():  #items() показывает содержимое словаря
    print(f"{country} - {capital}")
print("б) Столица Франции:")
print(countries["Франция"])  #обращение к словарю по ключу
print("в) Страны в алфавитном порядке:")
for country in sorted(countries.keys()):  # sorted() сортирует список стран
    print(f"{country} - {countries[country]}")


print("2 задание")
points = {
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10
}
word = input("Введите слово: ")
word = word.upper()  #перевод слова в заглавные буквы(ерхний регистр)
сумма_очков = 0
for letter in word:
        сумма_очков += points[letter]
print(f"стоимость слова '{word}': {сумма_очков} очков")


print("3 задание")
# Исходные данные: студенты и языки, которые они знают
students_languages = {
    "Мария": {"английский", "французский", "китайский"},
    "Влад": {"английский", "испанский"},
    "Светлана": {"китайский", "немецкий"},
    "Николай": {"русский", "английский", "китайский"},
    "Василий": {"французский", "итальянский"}
}
all_languages = set()  #пустое множество

for languages in students_languages.values():
    all_languages.update(languages)  #добавляем все языки из каждого студента
print("Все языки, которые знают студенты:")
for lang in sorted(all_languages):
    print(f" {lang}")

print(f"\nВсего различных языков: {len(all_languages)}")

# 3. Находим студентов, которые знают китайский язык
chinese_students = []

for student, languages in students_languages.items():
    if "китайский" in languages:  # проверяем, есть ли китайский в множестве языков студента
        chinese_students.append(student)

# Выводим результат
print(f"\nСтуденты, знающие китайский язык ({len(chinese_students)} чел.):")
for student in sorted(chinese_students):  # сортируем для красоты
    print(f"  • {student}")