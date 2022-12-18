

# годовая процентная ставка
# yearRate = 5/100  
yearRate = int(input("Введите процентную ставку: ")) / 100

# текущй размер депозита руб
# depositRub = 1000 
depositRub = int(input("Введите текущий размер депозита в рублях: "))

# копеек в депозите 

depositKop = int(input("Введите количество копеек в сумму депозита: "))

incrRateRub = int(depositRub * yearRate + depositRub)
incrRateKop = int(depositKop * yearRate + depositKop)


print("Вклад через год: ", incrRateRub, " руб ", incrRateKop, " коп")
