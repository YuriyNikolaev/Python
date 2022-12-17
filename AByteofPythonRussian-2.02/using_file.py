# Filename using_file.py

poem = '''\
Программировать это весело.
Если работа скучна, 
Чтобы придать ей веселый тон -
   используй Python!
'''

f = open('/home/yurich/PycharmProjects/untitled/venv/poem.txt', 'w') # открываем для записи (writing)
f.write(poem) # записываем текст в файл
f.close() # закрываем файл

f = open('/home/yurich/PycharmProjects/untitled/venv/poem.txt') # если не указан режим, по умолчанию подразумевается
                     # режим чтения ('r'eading)

while True:
    line = f.readline()
    if len(line) == 0: # нулевая длина обозначает конец файла (EOF)
        break
    print(line, end='')

f.close() # закрываем файл