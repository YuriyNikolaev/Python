# 02-theme_04-02-ex02.py
import random
print("Привет! Я твой чат-бот")
text = ""

while text != "выход":
    print("Поговори со мной!")
    text_meeting = input()
    
    while text_meeting in ["Привет","Здравствуй","Приветушки","привет","здравствуй","приветушки"]:
        print("Что вы хотите сделать?")
        text_action = input()
        
        while text_action in ["Поговорить","Поболтать","поболтать","поговорить"]:
            print("О чем хотите поговорить?")
            text_theme = input()

            if text_theme in ["дождь", "слякоть", "плохая", "Дождь", "Слякоть", "Плохая", "Снег", "снег", "Сильный ветер", "сильный ветер"]:
                print("Сочувствую! Наверное, вы мечтаете о солнце.")
                text_weather = input()

                if text_weather in ["Да", "да", "Вы правы", "вы правы"]:
                    print("Надеюсь скоро распогодится!")
                elif text_weather in ["Нет", "нет", "Вы не правы", "вы не правы"]:
                    print("В таком случае я рад, что вы не грустите в такую погоду!")
                else:
                    print("Я не понял вас")
            elif text_weather in ["Солнце", "солнце", "Жара", "жара", "Хорошая", "хорошая"]:
                print("Вау! Наверное, вы рады теплу?")
                text_weather = input()        