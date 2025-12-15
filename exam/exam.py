import concurrent.futures
import time
import random

FILES_TO_PROCESS = range(1, 11)
MAX_WORKERS = 4

def process_file(file_id):
    work_time = random.uniform(0.2, 0.6)
    time.sleep(work_time)

    if file_id == 5:
        raise Exception(f"File {file_id}")

    return f"File {file_id}|{work_time:.2f} sec"

if __name__ == "__main__":
    results = []
    errors = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:

        tasks = {pool.submit(process_file, file_id): file_id for file_id in FILES_TO_PROCESS}

        for future in concurrent.futures.as_completed(tasks):
            file_id = tasks[future]
            try:
                data = future.result()
                results.append(data)
            except Exception as error:
                errors.append(f"File {file_id} failed")
    
    for i in sorted(results):
        print(i)

    print(f"Errors {len(errors)}")
    for i in errors:
        print(f"{i}")