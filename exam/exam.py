import concurrent.futures
import time
import random
import os
from pathlib import Path

FILE_NAMES = [f"data_task_{i}.txt" for i in range(1, 11)] 
MAX_WORKERS = 4 
TEST_CONTENT = "word" * 10

def create_test_files():
    for name in FILE_NAMES:
        with open(name, 'w') as f:
            f.write(TEST_CONTENT)

def cleanup_files():
    for name in FILE_NAMES:
        file_path = Path(name)
        if file_path.exists():
            os.remove(file_path)

def process_file(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        
    work_time = random.uniform(0.2, 0.6)
    time.sleep(work_time)

    if "data_task_5" in file_name:
        raise Exception("Помилка обробки")

    return f"Файл {file_name} оброблено за {work_time:.2f} сек"

if __name__ == "__main__":
    create_test_files()
    results = []
    errors = []

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:

            tasks = {pool.submit(process_file, file_name): file_name for file_name in FILE_NAMES}

            for future in concurrent.futures.as_completed(tasks):
                file_name = tasks[future]
                try:
                    data = future.result()
                    results.append(data)
                except Exception as error:
                    errors.append(f"Файл {file_name} ЗБІЙ")
    
    finally:
        cleanup_files()
        
    for i in sorted(results):
        print(i)

    print(f"Errors {len(errors)}")
    for i in errors:
        print(f"{i}")