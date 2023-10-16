'''
Пробелы
В предложение были добавлены лишние пробелы. Напишите функцию, которая будет принимать 
такое предложение и возвращать его же в исправленном виде.
'''
# def cor_sentence(sentence):
#   words = sentence.split()
#   corrected_sentence = ' '.join(words)
#   return corrected_sentence

# sentence = "Helloo      world   !"
# corrected_sentence = cor_sentence(sentence)
# print(corrected_sentence)


'''
Прямоугольник
Напишите функцию, которая будет принимать два числа: ширину и высоту прямоугольника и возвращает  перимертр и площадь
'''
# def rectangle(a, b):
#     p = (a + b)*2
#     s = a * b
#     return p, s

# p, s = rectangle(5, 8)

# print(f"Периметр прямоугольника: {p}")
# print(f"Площадь прямоугольника: {s}")

'''
Буквы-подруги
Напишите функцию, которая будет принимать строку и две буквы. Функция должна проверять, всегда ли после первой переданной буквы идет вторая.
Например:

привет, пр ---> return True
привет, пт ---> return False

'''
# def letters_friends(string, letter_1, letter_2):
#     for i in range(len(string)):
#         if string[i] == letter_1 and string[i + 1] == letter_2:
#             return True
#     return False

# result = letters_friends(
# 	input("Введите строку: "),
# 	input("Введите первую букву: "),
# 	input("Введите вторую букву: "),
# )

# if result: 
#     print("После первой буквы следует вторая.")
# else:
#     print("После первой буквы не следует вторая.")
'''
Сборка машинок
Вы занимаетесь сборкой игрушечных машинок. Каждая машинка должна иметь четыре колеса, один корпус и две фигурки человечков внутри.
Фнукция должна возвращать строку в виде машинки (многострочная строка)
'''
# def create_car():
#     car = [
               
#           '┏┓|||| |||||',
#            '┃┃╭┻┻━━━┻━┻┏┓',
#            '┃┣╯┉┉╭━━┓╭┉┃┃',
#         '┃┣╮┉┉╰━━┛╰┉┃┃',
#          '┃┃╰┳┳━━━┳━┳┗┛',
#          '┗┛|||| |||||'
#     ]
#     car = '\n'.join(car)
#     return car


# car = create_car()
# print(car)
    
 


'''
Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает его же, меняя первую букву на большую.
Например, print(capitalize('word')) должно печатать слово Word.
'''
# def capitalize(word):
#     return word[0].upper() + word[1:]

# print(capitalize('word')) 


'''
На вход подаётся строка, состоящая из слов, разделённых одним пробелом. Слова состоят из маленьких латинских букв. Напечатайте исходную строку, сделав так, чтобы каждое слово начиналось с большой буквы. При этом используйте вашу функцию capitalize().

Напомним, что в Питоне есть функция ord(), которая по символу возвращает его код в таблице ASCII, и функция chr(), которая по коду символа возвращает сам символ. Например, ord('a') == 97, chr(97) == 'a'.
'''
# def capitalize(word):
#         return word[0].upper() + word[1:]
    
# cptlz = 'hello world' 
# words = cptlz.split()

# string = ' '.join(words)
# print(string)

'''
Создайте простейшую в мире функцию simple_func, а затем выведите на экран ее тип.
'''
# def simple_func():
#     pass

# print(type(simple_func))

'''


не изменяя структуры кода, запусти func_3
'''
# def func_1():
#   def func_2():
#     def func_3():
#       print('OK')
#     func_3()  
#   func_2()
# func_1()

'''
Напишите функцию, которая будет генерировать случайный пароль. В пароле должно быть от 8 до 15 символов
'''
# import random
# import string

# def random_password():
#   len_password = random.randint(8, 15)  
#   symbols = string.ascii_letters + string.digits
#   password = ''.join(random.choice(symbols) 
#   for i in range(len_password))

#   return password

# print(random_password)


import random

def random_password():
    password = ''
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    numbers = '1234567890'
    symbols = '!@#$%^&*-_'
    len_password = random.randint(8, 15)  
    isCorrect = [False, False, False, False]

    while isCorrect != [True, True, True, True]:
        for i in range(0, len_password+1):
            elements = random.randint(1,4)

            if elements == 1:
                password += random.choice(numbers)

            elif elements == 2:
                password += random.choice(symbols)

            elif elements == 3:
                password += random.choice(letters.upper())

            else:
                password += random.choice(letters.lower())

        print(password)

        isCorrect = [False, False, False, False]

        for let in password:
            if let in letters.upper():
                isCorrect[2] == True
                
            elif let in letters.lower():
                isCorrect[3] == True

            elif let in symbols:
                isCorrect[1] == True

            elif let in numbers:
                isCorrect[0] == True

        random_password()