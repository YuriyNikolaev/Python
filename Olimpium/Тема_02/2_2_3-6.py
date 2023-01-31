# 2_2_3-6.py

# Удалить из строки все символы, заключенные в скобки.



my_string = "abcd(123)efg"
new_string = " "
srez = my_string["(":")"]

for i in my_string:
    print(i, end=",")
    if i in srez:
        continue
    else:
        new_string += i

print(new_string)
    
        

# print(my_string)


 


