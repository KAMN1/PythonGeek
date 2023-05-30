#Пользователь вводит кол-во строк, затем сами строки. 
#Нужно записать в новый текстовый файл все эти строки
# Далее пользователь вводит символ, нужно найти кол-во этого символа в новом файлx

# x = int(input())
# string_list = []
# for i in range(x):
#     string_list.append (input(f'{i}:')+'\n')
# with open('example.txt', 'w', encoding="utf-8") as file:
#     file.writelines(string_list)

# symbol = input('введите символ:'+'\n')
# k=0
# with open('example.txt', 'r', encoding="utf-8") as file:
#     find = file.read()
#     for i in find:
#         if i == symbol:
#             k+=1
# print(k)


#документ «article.txt» содержит следующий текст:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).


# with open('article.txt', 'r', encoding="utf-8") as file:
#     find = file.read().replace('\n', ' ')
# list_text = find.split(" ")
# print(list_text)
# len_text = list(map(len, list_text))
# max_words = list(filter(lambda x: len(x) == max(len_text), list_text))
# print(max_words)

# Напишите функцию read_last(lines, file), 
# которая будет открывать определенный файл file и
# выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


def read_last(lines, file):
    with open(file, 'r', encoding="utf-8") as file:
        file_text = file.read().split("\n")
    print(file_text[-lines::])

read_last(int(input("введите кол-во строк"+ "\n")), "article.txt")
