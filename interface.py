import flet as ft
from functions import create, makedir, changedir, copy, delete, file_counter, analyse


def execute_function(func, output, *args):
    """Берет на вход функцию с аргументами и выполняет"""
    try:
        result = func(*args)
        output.controls.append(ft.Text(result, color='green'))
    except Exception as e:
        output.controls.append(ft.Text(f'Ошибка: {str(e)}', color='red'))
    output.update()

def main(page: ft.Page):
    page.title = 'Файловый менеджер'
    page.window_width = 200
    page.window_height = 600
    page.update()

    output = ft.Column()

    # Создание файла
    file_name = ft.TextField(label='Имя файла')
    file_content = ft.TextField(label='Текст', multiline=True)
    create_file_btn = ft.ElevatedButton('Создать файл', on_click=lambda _: execute_function(create, output, file_name.value, file_content.value))

    # Создание папки
    dir_name = ft.TextField(label='Имя папки')
    create_dir_btn = ft.ElevatedButton('Создать папку', on_click=lambda _: execute_function(makedir, output, dir_name.value))

    # Смена папки
    dir_name_change = ft.TextField(label='Имя папки куда переместиться')
    change_dir_btn = ft.ElevatedButton('Переместиться в папку', on_click=lambda _: execute_function(changedir, output, dir_name.value))

    # Копирование файла
    file_src = ft.TextField(label='Файл для копирования')
    file_dest = ft.TextField(label='Новое имя файла')
    copy_btn = ft.ElevatedButton('Копировать', on_click=lambda _: execute_function(copy, output, file_src.value, file_dest.value))

    # Удаление папки или файла
    delete_name = ft.TextField(label='Файл/папка для удаления')
    delete_btn = ft.ElevatedButton('Удалить', on_click=lambda _: execute_function(delete, output, delete_name.value))

    # Подсчет файлов
    count_btn = ft.ElevatedButton('Подсчет файлов', on_click=lambda _: execute_function(file_counter, output))

    # Анализ файлов
    analyse_btn = ft.ElevatedButton('Анализ файлов (размер)', on_click=lambda _: execute_function(analyse, output))


    # Размещение элементов на странице
    page.add(
        ft.Column([
            ft.Text('Файловый менеджер', size=15, weight=ft.FontWeight.BOLD),

            file_name, file_content, create_file_btn,
            dir_name, create_dir_btn,
            dir_name_change, change_dir_btn,
            file_src, file_dest, copy_btn,
            delete_name, delete_btn,
            count_btn,
            analyse_btn,

            output
        ], spacing=5)
    )

ft.app(target=main)
