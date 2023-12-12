import os
import shutil
import time

def is_file_modified_within_24_hours(file_path):
    current_time = time.time()
    twenty_four_hours_ago = current_time - 24 * 60 * 60

    file_stat = os.stat(file_path)
    modified_time = max(file_stat.st_mtime, file_stat.st_ctime)

    return modified_time > twenty_four_hours_ago

def update_and_move_files():
    current_directory = os.getcwd()
    last_24hours_directory = os.path.join(current_directory, 'last_24hours')

    if not os.path.exists(last_24hours_directory):
        os.mkdir(last_24hours_directory)

    files = os.listdir(current_directory)

    for file_name in files:
        file_path = os.path.join(current_directory, file_name)

        if os.path.isfile(file_path) and is_file_modified_within_24_hours(file_path):
            destination_path = os.path.join(last_24hours_directory, file_name)
            shutil.copy2(file_path, destination_path)
            print(f"Updated and moved file: {file_name}")

update_and_move_files()