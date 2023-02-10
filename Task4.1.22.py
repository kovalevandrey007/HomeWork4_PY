# 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Если таких чисел нет - выдать внятное диагностическое сообщение


# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры
# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

list1 = '2 4 6 8 10 12 10 8 6 4 2'
list2 = '3 6 9 12 15 18'
list3 = []
for idx1, el1 in enumerate(list1.split()):
    for idx2, el2 in enumerate(list2.split()):
        if el1 == el2 and idx1 <= len(list1) and idx2 <= len(list2):
            list3.append(el1)
        else:
            idx1 += 1
            idx2 += 1
print(" ".join(set(list3)))

# text = 'a a a b c a a d c d d'
# text = text.split()
# result = ''
# dict1 = {}
# for i in range(len(text)):
#     if text[i] not in dict1:
#         dict1[text[i]] = 1
#         result += f'{text[i]} '
#     else:
#         dict1[text[i]] += 1
#         result += f'{text[i]}_{dict1[text[i]] - 1} '
#
# print(result)