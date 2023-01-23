# 2_2-4.py
# Отредактировать предложение, удаляя из него лишние пробелы, 
# оставляя только по одному пробелу между словами.

input_str = " удаляя   из него  лишние   пробелы    "
temp = input_str.split()
print(temp) 

new_str = temp.split(" ")
print(new_str) 

# new_str = ""

# for i in input_str:
#     # print(i, end="-")
#     if i != " ":
#         new_str += i
#     print(new_str)    

