# Python-программа для объяснения метода os.mkdir ()

# импорт модуля os

import os


# Каталог

directory = "GeeksForGeeks"


# Путь к родительскому каталогу

parent_dir = "/home/yurich/"

# Путь

path = os.path.join(parent_dir, directory)


# Создать каталог
# 'GeeksForGeeks' в
# '/ home / Пользователь / Документы'
os.mkdir(path)

print("Directory '%s' created" %directory)


# Каталог

directory = "ihritik"


# Путь к родительскому каталогу

parent_dir = "/home/yurich/"


# Режим

mode = 0o666

# Путь

path = os.path.join(parent_dir, directory)

# Создать каталог
# 'GeeksForGeeks' в 
# '/ home / yurich'
# с режимом 0o666
os.mkdir(path, mode)


