# Practice 6: Python File Handling and Built-in Functions
## 1. File modes: r, w, a, x
1. **r — Read (Чтение)**
Opens the file for reading only.The file must exist, otherwise it will raise an error.Does not allow modifying the content.
Открывает файл только для чтения.Файл должен существовать, иначе будет ошибка.Не позволяет изменять содержимое.
```bash
with open("example.txt", "r") as f:
    content = f.read()  # read the entire file / читаем весь файл
```

2. **w — Write (Запись)**
Opens the file for writing.If the file does not exist, it creates a new one.If the file exists, it completely overwrites it.
Открывает файл для записи.Если файла нет → создаёт новый.Если файл существует → полностью перезаписывает его.
```bash
with open("example.txt", "w") as f:
    f.write("Hello World")  # overwrite the file / файл перезаписан
```

3. **a — Append (Добавление)**
Opens the file for adding text at the end.Existing content is preserved.If the file does not exist, it creates a new one.
Открывает файл для добавления текста в конец.Существующее содержимое сохраняется.Если файла нет → создаёт новый.
```bash
with open("example.txt", "a") as f:
    f.write("\nNew line added")  # append to the end / добавление в конец файла
```

4. **x — Exclusive Creation (Создание нового файла)**
Opens the file only for creating a new file.If the file already exists, it will raise a FileExistsError.Used when you want to guarantee not to overwrite an existing file.
Открывает файл только для создания нового файла.Если файл уже существует → будет ошибка FileExistsError.Используется, когда нужно гарантировать, что старый файл не будет перезаписан.
```bash
with open("new_file.txt", "x") as f:
    f.write("This file is newly created")  # new file created / создаётся новый файл
```

---

## 2. Reading files: read(), readline(), readlines()
1. **read() — Read entire file / Чтение всего файла**
Reads the entire file as a single string.
Читает всё содержимое файла как одну строку.
```bash
with open("example.txt", "r") as f:
    content = f.read()  # read entire file / читаем весь файл
    print(content)
```

2. **readline() — Read one line at a time / Чтение одной строки**
Reads the next line from the file each time it is called.
Читает одну строку за раз.
```bash
with open("example.txt", "r") as f:
    line1 = f.readline()  # first line / первая строка
    line2 = f.readline()  # second line / вторая строка
    print(line1, line2)
```

```💡 Note / Примечание:

Use it in a loop to read file line by line.
Используется в цикле, чтобы читать файл построчно:```

```bash
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())  # remove newline / убираем перевод строки
```

3. **readlines() — Read all lines as a list / Чтение всех строк как список**
Reads all lines and returns them as a list of strings.
Читает все строки и возвращает список строк.
```bash
with open("example.txt", "r") as f:
    lines = f.readlines()  # all lines / все строки в списке
    print(lines)
```

---
## 3. Writing and appending files
1. **write() — Write a string / Запись строки**
Writes a string to a file.
Записывает строку в файл.
```bash
with open("example.txt", "w") as f:
    f.write("Hello Python\n")  # write a single line / записываем одну строку
```

2. **writelines() — Write a list of strings / Запись списка строк**
Writes a list of strings to a file.
Записывает список строк в файл.
```bash
lines = ["Hello\n", "Python\n", "World\n"]
with open("example.txt", "w") as f:
    f.writelines(lines)  # write all lines / записываем все строки
```

3. **Append mode a — Add text to the end / Режим добавления a**
Opens the file to add text at the end without deleting existing content.
Открывает файл для добавления текста в конец, не удаляя старое содержимое.
```bash
with open("example.txt", "a") as f:
    f.write("Appending a new line\n")  # append text / добавляем новую строку
```

---

## 4. Context manager: with statement
1. **Using with to handle files / Использование with для работы с файлами**
The with statement automatically closes the file after the block, even if an error occurs.
Оператор with автоматически закрывает файл после блока, даже если возникает ошибка.
```bash
with open("example.txt", "r") as f:
    content = f.read()  # read the file / читаем файл
print(content)

# no need to call f.close() / не нужно вызывать f.close()
```

2. **Writing with with / Запись с with**
```bash
with open("example.txt", "w") as f:
    f.write("Hello Python\n")  # write to the file / записываем в файл
```

No need to call f.close(), the file is automatically closed.
Не нужно вызывать f.close(), файл закрывается автоматически.

3. **Appending with with / Добавление с with**
```bash 
with open("example.txt", "a") as f:
    f.write("Appending a new line\n")  # append text / добавляем текст в конец
```

Existing content is preserved, and the file is safely closed after the block.
Старое содержимое сохраняется, а файл безопасно закрывается после блока.

---

## 5. File and path operations: os, shutil, pathlib
1. **os module / Модуль os**
Provides functions to interact with the operating system.
Предоставляет функции для взаимодействия с операционной системой.
```bash
import os

# Current working directory / Текущая рабочая директория
print(os.getcwd())  # e.g., /home/user

# List files and directories / Список файлов и папок
print(os.listdir("."))  # list in current directory / список текущей папки

# Create a directory / Создать папку
os.mkdir("new_folder")

# Remove a file / Удалить файл
os.remove("example.txt")

# Rename a file / Переименовать файл
os.rename("old.txt", "new.txt")
```

2. **shutil module / Модуль shutil**
Provides functions to copy, move, and remove files and directories.
Предоставляет функции для копирования, перемещения и удаления файлов и папок.
```bash
import shutil

# Copy a file / Копирование файла
shutil.copy("source.txt", "destination.txt")

# Move a file or directory / Перемещение файла или папки
shutil.move("file.txt", "folder/")

# Remove a directory with all contents / Удалить папку с содержимым
shutil.rmtree("old_folder")
```

3. **pathlib module / Модуль pathlib**
Provides object-oriented paths and convenient methods.
Предоставляет объектно-ориентированные пути и удобные методы.
```bash
from pathlib import Path

# Path object / Объект пути
p = Path("example.txt")

# Check if file exists / Проверка существования файла
print(p.exists())  # True / False

# Read file / Чтение файла
print(p.read_text())  

# Write file / Запись файла
p.write_text("Hello Pathlib\n")  

# Parent directory / Родительская папка
print(p.parent)

# Combine paths / Объединение путей
new_file = p.parent / "new_file.txt"
print(new_file)
```

----

## 6. Directory management: os.mkdir(), os.makedirs(), os.listdir(), os.chdir(), os.getcwd(), os.rmdir()
1. **os.mkdir() — Create a single directory / Создать одну папку**
Creates a new directory at the specified path.
Создаёт новую папку по указанному пути.
```bash
import os

os.mkdir("new_folder")  # create a folder / создаём папку
```

2. **os.makedirs() — Create nested directories / Создать вложенные папки**
Creates nested directories, creating any missing parent directories.
Создаёт вложенные папки, создавая все отсутствующие родительские папки.
```bash
os.makedirs("parent/child/grandchild")  # create nested folders / создаём вложенные папки
```
```
💡 Note / Примечание:

Can use exist_ok=True to avoid errors if directory exists.

Можно использовать exist_ok=True, чтобы не получать ошибку, если папка уже есть.
```

3. **os.listdir() — List contents of a directory / Список содержимого папки**
Returns a list of files and directories in the specified path.
Возвращает список файлов и папок по указанному пути.
```bash
print(os.listdir("."))  # list current folder / список текущей папки
```
4. **os.chdir() — Change current working directory / Смена рабочей директории**
Changes the current working directory to the specified path.
Меняет текущую рабочую папку на указанную.
```bash
os.chdir("new_folder")  # change directory / переходим в папку
print(os.getcwd())  # check current directory / проверяем текущую директорию
```

5. **os.getcwd() — Get current working directory / Текущая рабочая директория**
Returns the current working directory.
Возвращает текущую рабочую папку.
```bash
cwd = os.getcwd()
print(cwd)  # e.g., /home/user / пример: /home/user
```
6. **os.rmdir() — Remove an empty directory / Удаление пустой папки**
Removes an empty directory at the specified path.
Удаляет пустую папку по указанному пути.
```bash
os.rmdir("old_folder")  # remove folder / удаляем папку
```
```
💡 Note / Примечание:

The directory must be empty, otherwise OSError occurs.

Папка должна быть пустой, иначе будет ошибка OSError.
```

## 7. Built-in functions: len(), sum(), min(), max(), map(), filter(), reduce(), enumerate(), zip(), sorted(), type conversion functions
1. **len() — Length / Длина**
Returns the length of a sequence or collection.
Возвращает длину последовательности или коллекции.
```bash
my_list = [1, 2, 3, 4]
print(len(my_list))  # 4 / длина списка
```

2. **sum() — Sum / Сумма**
Returns the sum of all elements in an iterable.
Возвращает сумму всех элементов итерируемого объекта.
```bash
numbers = [10, 20, 30]
print(sum(numbers))  # 60 / сумма элементов
```

3. **min() and max() — Minimum and Maximum / Минимум и Максимум**
Returns the smallest or largest element.
Возвращает наименьший или наибольший элемент.
```bash
values = [5, 1, 9, 3]
print(min(values))  # 1 / минимум
print(max(values))  # 9 / максимум
```

4. **map() — Apply function / Применить функцию**
Applies a function to each element of an iterable.
Применяет функцию к каждому элементу итерируемого объекта.
```bash
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9] / квадраты чисел
```

5. **filter() — Filter elements / Фильтрация элементов**
Filters elements in an iterable using a condition function.
Фильтрует элементы итерируемого объекта по условию.
```bash
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4] / только чётные
```

6. **reduce() — Reduce iterable / Сведение последовательности**
Reduces an iterable to a single value using a function.
Сводит последовательность к одному значению с помощью функции.
```bash
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x*y, nums)
print(product)  # 24 / произведение всех элементов
```

7. **enumerate() — Enumerate / Нумерация элементов**
Returns pairs of index and element from an iterable.
Возвращает пары индекс–элемент из последовательности.
```bash
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry
```

8. **zip() — Combine iterables / Объединение последовательностей**
Combines two or more iterables element-wise.
Объединяет две или более последовательностей поэлементно.
```bash
names = ["Alice", "Bob"]
ages = [25, 30]
combined = list(zip(names, ages))
print(combined)  # [('Alice', 25), ('Bob', 30)]
```

9. **sorted() — Sort / Сортировка**
Returns a sorted list from an iterable.
Возвращает отсортированный список из последовательности.
```bash
numbers = [4, 1, 3]
print(sorted(numbers))  # [1, 3, 4] / отсортированный список
```

10. **Type conversion functions / Преобразование типов**
Convert data between int, float, str, list, tuple etc.
Преобразование данных между int, float, str, list, tuple и др.
```bash
print(int("10"))    # 10 / строка в число
print(float("3.14"))  # 3.14 / строка в число с плавающей точкой
print(str(123))     # '123' / число в строку
print(list((1,2,3))) # [1,2,3] / к списку
print(tuple([1,2,3])) # (1,2,3) / к кортежу
```

