import datetime
import os
import random
import string

'''creates and returns a random file name prefixed with prefix'''
def create_random_name(prefix) -> str:
    random_string = prefix + ''.join(random.choices(string.ascii_lowercase, k=3))
    return random_string


def create_custom_file(file_name, size_of_the_file):
    filler_word = b'filler'
    size_of_the_file_bytes = size_of_the_file*1024*1024
    file_dump_dir = os.path.join("storage_automated_tests", "sample_files")
    print('file_dump_dir is ', file_dump_dir)

    os.makedirs(file_dump_dir, exist_ok=True)

    file_path = os.path.join(file_dump_dir,file_name)
    with open(file_path, 'wb') as file:
        file.write(filler_word * (size_of_the_file_bytes//len(filler_word)))


create_custom_file('simple_file', 5)