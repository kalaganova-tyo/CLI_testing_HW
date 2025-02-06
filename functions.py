#import sys
import argparse
import shutil
import os


def create(file_name, text: str):
    """Create new txt file"""
    with open(file_name, 'w') as file:
        file.write(text)


def copy(file_name, new_file_name):
    shutil.copy(file_name, new_file_name)


def delete(file_name):
    os.remove(file_name)


parser = argparse.ArgumentParser('Simple file manager')

subparsers = parser.add_subparsers(dest='command', required=True)

parser_add = subparsers.add_parser(name='create', help='Create some text file')
parser_add.add_argument('file_name', type=str, help='Name for new file')
parser_add.add_argument('text', type=str, help='Text in file')
parser_add.set_defaults(func=create)

parser_sub = subparsers.add_parser(name='copy', help='Copy your file')
parser_sub.add_argument('file_name', type=str, help='File for copy')
parser_sub.add_argument('new_file_name', type=str, help='New name for copy file')
parser_sub.set_defaults(func=copy)

parser_sub = subparsers.add_parser(name='delete', help='Delete file')
parser_sub.add_argument('file_name', type=str, help='File for delete')
parser_sub.set_defaults(func=delete)

argv = parser.parse_args()

if argv.command == 'create':
    argv.func(argv.file_name, argv.text)
elif argv.command == 'copy':
    argv.func(argv.file_name, argv.new_file_name)
elif argv.command == 'delete':
    argv.func(argv.file_name)
