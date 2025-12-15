import concurrent.futures # Для пулу потоків
import time                # Для імітації затримки
import random              # Для випадкових затримок
import os                  # Для роботи з файловою системою (видалення)
from pathlib import Path   # Для роботи зі шляхами

FILE_NAMES = [f"data_task_{i}.txt" for i in range(1, 11)] # 10 реальних імен файлів
MAX_WORKERS = 4                                           # Кількість потоків-робітників
TEST_CONTENT = "Test data for processing. " * 10          # Вміст для файлів

def create_test_files(): # Функція створює 10 файлів на диску
    for name in FILE_NAMES:
        with open(name, 'w') as f:
            f.write(TEST_CONTENT)

def cleanup_files(): # Функція видаляє всі створені файли
    for name in FILE_NAMES:
        file_path = Path(name)
        if file_path.exists():
            os.remove(file_path)

def process_file(file_name): # Обробка одного файлу в окремому потоці
    with open(file_name, 'r') as f:
        content = f.read()   # 1. Блокуюча I/O операція (читання)
        
    work_time = random.uniform(0.2, 0.6)
    time.sleep(work_time)    # 2. Імітація обробки (звільняє GIL)

    if "data_task_5" in file_name:
        raise Exception("Помилка обробки") # 3. Імітація збою

    return f"Файл {file_name} оброблено ({len(content)} символів) за {work_time:.2f} сек"

if __name__ == "__main__":
    
    create_test_files() # Створюємо файли перед запуском

    results = []
    errors = []

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool: # Ініціалізація пулу 

            tasks = {pool.submit(process_file, file_name): file_name for file_name in FILE_NAMES} # Надсилання 10 завдань

            for future in concurrent.futures.as_completed(tasks): # Збір результатів у порядку готовності
                file_name = tasks[future]
                try:
                    data = future.result()                       # Отримання результату (може викликати виняток)
                    results.append(data)
                except Exception as error:
                    errors.append(f"Файл {file_name} ЗБІЙ")      # Ізоляція помилки
    
    finally:
        cleanup_files() # Гарантоване видалення файлів (навіть при помилці)
        
    for i in sorted(results):
        print(i)

    print(f"Errors {len(errors)}") # Виведення загальної статистики
    for i in errors:
        print(f"{i}")