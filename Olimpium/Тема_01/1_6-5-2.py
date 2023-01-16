n=int(input("Введите первое число "))
m=int(input("Введите второе число "))
s1=0
for i in range(1,n):
   if n%i==0:
       s1+=i
s2=0
for i in range(1,m):
   if m%i==0:
       s2+=i
if (s1==m) and (s2==n):
    print("yes")
else:
    print("no")