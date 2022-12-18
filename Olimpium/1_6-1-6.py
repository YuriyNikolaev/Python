dec=int(input("Введите десятичное число "))
v=128
for i in range(1,9):
    if dec>=v:
        print('1', end='')
        dec=dec-v
    else:
        print('0', end='')
    v=v//2