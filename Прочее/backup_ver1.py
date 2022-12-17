# Filename backup_ver1.py

import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\Tmp"', 'C:\\Tmp']
# Заметьте, что для имен, содержащих внутри пробелы, необходимо использовать
# двойные ковычки внутри строки

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\Tmp2' # Подставьте ваш путь

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-фрхива служит текущая дата и время.
target = target_dir + os.sep + time.strftime('%Y%m%a%H%M%S') + '.zip'

# 5. Используйте команду "zip" для перемещения файлов в zip-фрхив
zip_command = "zip -qr {0} {1}" .format(target, ' '.join(source))

# Запускаем создание резервной копии
print(zip_command)

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в ', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
