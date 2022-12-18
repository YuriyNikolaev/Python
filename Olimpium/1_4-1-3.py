#x = -5
x = int(input("Введите координату х: "))
#y = 6
y = int(input("Введите координату у:"))

if( x > 0 and y > 0):
    print("1я четверть")
elif(x > 0 and y < 0):
    print("2я четверть")
elif(x < 0 and y < 0):
    print(("3я четверть"))
else:
    print("4я четверть")