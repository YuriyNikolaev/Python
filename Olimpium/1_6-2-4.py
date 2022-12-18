k=int(input("Введите число "))
print(k,'= ')
l=2
while not(k==1):
    if k%l==0:
        k=k/l
        print(l, end=' ')
    else:
        l+=1