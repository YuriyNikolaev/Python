n = int(input("число? "))


#print("%", n % 2)

if(n % 2 != 0):
    print("YES")
else:
    if(2 < n <= 5):
        print("No")
    elif(6 <= n <= 20):
        print("YES")
    elif(n > 20):
        print("YES")

