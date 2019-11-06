import re
import sys
#import ctypes
from win32 import win32console
from colorama import Fore, init
#ctypes.windll.kernel32.SetConsoleTitleW('IDX2TXT')
win32console.SetConsoleTitle('IDX2TXT')
init()
print(Fore.GREEN + '    Обработка данных из IDX файла тахеометра\n\
    Leica Builder 509')
file_name = input('Введите путь к IDX файлу\
(C:\\F_21PG1.IDX): ')
file_input_name_check = file_name.replace('\"', '')
file_input_name = file_input_name_check.replace('\\', '/')
try:
    with open(file_input_name, 'r') as f:
        data = f.readlines()
except FileNotFoundError:
    print('Файл не найден!')
    input()
    sys.exit()
format_data = []
format_data1 = []
for row in data:
    row = row.replace('\n', '')
    row = row.replace('\t', '')
    result = re.match(r'\d{8}', row)
    if result:
        format_data.append(row)

for row in format_data:
    row_list = row.split(',')
    if len(row_list) == 8:
        row_list.pop(-1)
        row_list.pop(-1)
        row_list.pop(-1)
        row_list.pop(0)
        row_list[0] = row_list[0].replace('"', '')
        row = '\t'.join(row_list)
        format_data1.append(row)
print(Fore.RED + 'Точка\tY\t\tX\t\tZ')
for row in format_data1:
    print(Fore.YELLOW + row)
print(Fore.RED, end='')
answer = input('Сохранить файл (y/n)?:')
if answer == 'y':
    file_output_name = file_input_name.upper()
    file_output_name = file_output_name.replace('IDX', 'TXT')
    with open(file_output_name, 'w') as f:
        for row in format_data1:
            print(row, file=f)
    try:
        with open(file_output_name, 'r') as f:
            check = f.read()
        print(Fore.GREEN + 'Файл успешно сохранен!')
        print('    Enter для выхода')
    except FileNotFoundError:
        print(Fore.GREEN + 'Ошибка сохранения файла!')
        print('    Enter для выхода')
    input()
elif answer == 'n':
    print(Fore.GREEN + '    Enter для выхода')
    input()
else:
    sys.exit()
