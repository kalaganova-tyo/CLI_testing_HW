#import sys
import argparse
import shutil
import os


def create(file_name, text: str):
    """Create new txt file"""
    full_path = os.path.abspath(file_name)
    with open(full_path, 'w') as file:
        file.write(text)
    print(f'Файл {full_path} создан')


def makedir(dir_name):
    """Create new directory"""
    os.mkdir(dir_name)


def changedir(dir_name):
    """Change directory"""
    if not os.path.isdir(dir_name):
        print(f'ОшибкаОшибка: {dir_name} не найдена')
        return
    try:
        os.chdir(dir_name)
        print(f'Переместились в папку {os.getcwd()}')
    except Exception as e:
        print('Ошибка при смене директории')


def copy(file_name, new_file_name):
    """Copy file"""
    try:
        shutil.copy(file_name, new_file_name)
        print(f'{file_name} скопирован с новым названием {new_file_name}')
    except FileNotFoundError:
        print(f'{file_name} не существует для копирования')


def delete(file_or_dir):
    """Delete file or directory"""
    try:
        if os.path.isfile(file_or_dir):
            os.remove(file_or_dir)
            print(f'Файл {file_or_dir} удален')
        elif os.path.isdir(file_or_dir):
            shutil.rmtree(file_or_dir)
            print(f'Папка {file_or_dir} удалена')
    except FileNotFoundError:
        print(f'Файла или папки с таким названием {file_or_dir} не существует')


def file_counter(directory='.'):
    """Count of file in the directory"""
    all_files = 0
    try:
        for root, dirs, files in os.walk(directory):
            all_files += len(files)
        print(f'Всего файлов в папке {all_files}')
    except OSError:
        print(f'Папка {directory} не найдена')


def analyse(directory='.'):
    if not os.path.isdir(directory):
        print(f'Ошибка: {directory} такой папки не существует')
    for root, dirs, files in os.walk(directory):
        for file in files:
            path_to_file = os.path.join(root, file)
            try:
                file_size = os.path.getsize(path_to_file)
                print(f'Файл {file} имеет размер {file_size} байт')
            except OSError:
                print(f'Файл {file} поломан')


parser = argparse.ArgumentParser('Simple file manager')

subparsers = parser.add_subparsers(dest='command', required=True)

parser_add = subparsers.add_parser(name='create', help='Create some text file. You can make file in other directory <dir>/<file_name>')
parser_add.add_argument('file_name', type=str, help='Name for new file')
parser_add.add_argument('text', type=str, help='Text in file')
parser_add.set_defaults(func=create)

parser_add = subparsers.add_parser(name='makedir', help='Create new directory')
parser_add.add_argument('dir_name', type=str, help='Name for new directory')
parser_add.set_defaults(func=makedir)

parser_add = subparsers.add_parser(name='changedir', help='Change directory')
parser_add.add_argument('dir_name', type=str, help='Directory name to move on')
parser_add.set_defaults(func=changedir)

parser_sub = subparsers.add_parser(name='copy', help='Copy your file')
parser_sub.add_argument('file_name', type=str, help='File for copy')
parser_sub.add_argument('new_file_name', type=str, help='New name for copy file')
parser_sub.set_defaults(func=copy)

parser_sub = subparsers.add_parser(name='delete', help='Delete file')
parser_sub.add_argument('file_or_dir', type=str, help='File or directory for delete')
parser_sub.set_defaults(func=delete)

parser_sub = subparsers.add_parser(name='file_counter', help='Count all files in this directory and subdirectory')
parser_sub.set_defaults(func=file_counter)

parser_sub = subparsers.add_parser(name='analyse', help='All files size in this directory and subdirectory')
parser_sub.add_argument('directory', type=str, nargs='?', default='.', help='Directory for analyse, default = current')
parser_sub.set_defaults(func=analyse)

argv = parser.parse_args()

if argv.command == 'create':
    argv.func(argv.file_name, argv.text)
elif argv.command == 'makedir':
    argv.func(argv.dir_name)
elif argv.command == 'changedir':
    argv.func(argv.dir_name)
elif argv.command == 'copy':
    argv.func(argv.file_name, argv.new_file_name)
elif argv.command == 'delete':
    argv.func(argv.file_or_dir)
elif argv.command == 'file_counter':
    argv.func()
elif argv.command == 'analyse':
    argv.func(argv.directory)