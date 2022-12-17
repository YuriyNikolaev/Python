# Filename 28_IfSpiral.py
# Внес свои коррективы

answer = input("Хотите увидеть спираль? д/н: ")
if answer == 'д':
    print("Работаем")

    import turtle
    t = turtle.Pen()
    t.speed(0) # сам добавил
    t.width(3)
    for x in range(100):
        t.forward(x*4)
        t.left(89)
    print("Ну вот, готово!")

print("Ну ладно, пока!")  # сам добавил