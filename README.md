
#### CLI и тестирование

Простое консольное приложение

Функции:
- create - создает файл;
- makedir - создает папку;
- changedir - переходит в другую папку;
- copy - копирует файл;
- delete - удаляет файл или папку;
- file_counter - считает количество файлов в выбранной папке;
- analyse - выводит список всех файлов с размерами в байтах и общий вес.


#### Как использовать

Вызов в консоли:

    .\manager
            create <test.txt>
            makedir <testfolder>
            changedir <folder_name_for_change>
            copy <file_name> <new_name>
            delete <file_name_or_folder_name>
            file_counter <folder_name>
            analyse <folder_name>

