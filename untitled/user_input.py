# Filename user_input.py

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

somthing = input('Введите текст: ')
if (is_palindrome(somthing)):
    print("Да, это плиндром")
else:
    print("Нет, это не полиндром")