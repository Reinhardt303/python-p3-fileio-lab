import os

def write_file(file_name, file_content):
    with open(f'{file_name}', mode='w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}', mode='a') as file:
        file.write(append_content)

def read_file(file_name):
    with open(f'{file_name}', mode='r', encoding='utf-8') as file:
        return file.read()
