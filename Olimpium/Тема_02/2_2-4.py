# 2_2-4.py
# Отредактировать предложение, удаляя из него лишние пробелы, 
# оставляя только по одному пробелу между словами.

my_string = '  Удаляя   из него  лишние   пробелы.    '

my_list = my_string.split()
print( my_list )

new_list = " ".join(my_list)
print(new_list)