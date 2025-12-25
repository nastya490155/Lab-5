import re

file_path = "c:\\Users\\Ananastenka\\Desktop\\lab5\\task1-en.txt"

# Регулярные выражения
six_letter_words_regex = r"\b[a-zA-Zа-яА-ЯёЁ]{6}\b"  # слова из 6 букв
eight_letter_words_regex = r"\b[a-zA-Zа-яА-ЯёЁ]{8}\b"  # слова из 8 букв
all_numbers_regex = r"\b\d+(?:\.\d+)?\b"  # целые и дробные числа

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    six_letter_words = re.findall(six_letter_words_regex, content, re.IGNORECASE)
    eight_letter_words = re.findall(eight_letter_words_regex, content, re.IGNORECASE)
    all_numbers = re.findall(all_numbers_regex, content)
    
    # Вывод результатов
    print(f"Слова из 6 букв (найдено: {len(six_letter_words)}):")
    print(f"Слова из 8 букв (найдено: {len(eight_letter_words)}):")
    if six_letter_words:
        for word in six_letter_words:
            print(word)
    else:
        print("Не найдено слов из 6 букв")
    if eight_letter_words:
        for word in eight_letter_words:
            print(word)
    else:
        print("Не найдено слов из 8 букв")
    
    print(f"\nВсе числа (найдено: {len(all_numbers)}):")
    if all_numbers:
        for number in all_numbers: 
            print(number)
    else:
        print("Числа не найдены")
    
    # Дополнительная статистика
    print(f"\n--- Статистика ---")
    print(f"Всего слов из 6 букв: {len(six_letter_words)}")
    print(f"Всего слов из 8 букв: {len(eight_letter_words)}")
    print(f"Всего чисел: {len(all_numbers)}")
    
    # Разделение на целые и дробные
    integers = [n for n in all_numbers if '.' not in n]
    fractions = [n for n in all_numbers if '.' in n]
    print(f"Целых чисел: {len(integers)}")
    print(f"Дробных чисел: {len(fractions)}")

except FileNotFoundError:
    print(f"Файл по пути '{file_path}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
    

try:
    
    file_path1 = "c:\\Users\\Ananastenka\\Desktop\\lab5\\task2.html"
    with open(file_path1, "r", encoding="utf-8") as file:
        html_content = file.read()
    

    pattern = r'content\s*=\s*["\']([^"\']*)["\']'
    matches = re.findall(pattern, html_content, re.DOTALL | re.IGNORECASE)
    

    print(f"Найдено строк в атрибутах content: {len(matches)}")
    print("-" * 50)
    
    if matches:
        for i, content_value in enumerate(matches, 1):
            print(f"{i:2}. {content_value}")
    else:
        print("Атрибуты content не найдены в файле.")
except FileNotFoundError:
    print(f"Файл по пути '{file_path1}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
    
import re
import csv

input_file = r"c:\\Users\\Ananastenka\\Desktop\\lab5\\task3.txt"

output_file = r"c:\\Users\\Ananastenka\\Desktop\\lab5\\task3_normalized.csv"


regex_id = r'\b\d+\b'  
regex_email = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'  
regex_date = r'\b\d{4}-\d{2}-\d{2}\b'  
regex_url = r'\bhttps?://[^\s]+\b' 
regex_surname = r'\b[А-ЯЁA-Z][а-яёa-zA-Z-]+\b'  

try:

    with open(input_file, "r", encoding="utf-8") as file:
        data = file.read()

    # Extraer datos usando las expresiones regulares
    ids = re.findall(regex_id, data)
    emails = re.findall(regex_email, data)
    dates = re.findall(regex_date, data)
    urls = re.findall(regex_url, data)


    remaining_data = re.sub(f"{regex_id}|{regex_email}|{regex_date}|{regex_url}", "", data)
    surnames = re.findall(regex_surname, remaining_data)

    min_length = min(len(ids), len(surnames), len(emails), len(dates), len(urls))
    ids = ids[:min_length]
    surnames = surnames[:min_length]
    emails = emails[:min_length]
    dates = dates[:min_length]
    urls = urls[:min_length]

    with open(output_file, "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')  
        writer.writerow(["ID", "Фамилия", "Электронная почта", "Дата регистрации", "Сайт"])
        for i in range(min_length):
            writer.writerow([ids[i], surnames[i], emails[i], dates[i], urls[i]])

    print(f"Данные успешно обработаны и сохранены в файл: '{output_file}'")

except FileNotFoundError:
    print(f"Файл '{input_file}' не найден. Проверьте путь к файлу.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

