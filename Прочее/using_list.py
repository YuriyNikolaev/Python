#Filename using_list.py

#Это мой список покупок
shoplist = [' яблоки', ' манго', ' морковь', ' бананы']

print('я должен сделать', len(shoplist), 'покупки')

print('покупки', end= '')
for item in shoplist:
    print(item, end= '')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('отсортирую-ка я свой список')
shoplist.sort()
print('отсортированный список покупок выглядит так:', shoplist)

print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('я купил', olditem)
print('Теперь мой список покупок:', shoplist)
