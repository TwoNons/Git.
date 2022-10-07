# 3.1
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print (*my_list [-2])

# 3.2
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# result_2 = list(filter(lambda x: isinstance(x,str),list_1))
# print([item for item in result_2 if 'a' in item])
# result = filter(lambda x: isinstance(x,int),list_1)
# print(sum(result))

# 3.3
# list = ['cat', 'dog', 'horse', 'cow']
# name = 'cat', 'dog', 'horse', 'cow'
# list = name
# print(type(name),name)

# 3.4
# family_1 = input('Члены1: ').split(',')
# family_2 = input('Члены2: ').split(',')
# if len(family_1) > len(family_2):
#     print(f'Family 1 is bigger: {family_1}')
# elif len(family_2) == len(family_1):
#     print(f'Family_2 is equal Family_1: {"Equal"}')
# elif len(family_2) > len(family_1):
#     print(f'Family 2 is bigger: {family_2}')

# 3.5
# film_White_Bim_Black_Ear = {'title':'story',
#                             'director': 'Chernushenko',
#                             'year':'1978',
#                             'budget':'1000USD',
#                             'main_actor':'dog',
#                             'slogan':'not standard'}
# print(film_White_Bim_Black_Ear.items())
# print(film_White_Bim_Black_Ear.values())
# print(film_White_Bim_Black_Ear.keys())

# 3.6
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))

# 3.7
# print(*set([1, 2, 3, 4, 5, 3, 2, 1]))

# 3.8
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.issubset(set2))
# print(set1.intersection(set2)) #повторяется
# print(set1.difference(set2)) #не повторяется

#4.1
# import math
# def kvadrat(x):
#     P = x*4
#     S = x**2
#     D = math.sqrt(2)*x
#     return P, S, D
# print(kvadrat(10))

# 4.2
# def func (**kwargs):
#     return (kwargs)
# print(func(name = 'John', last_name = 'Smith', age = 35, position = 'web developer'))

#4.3
# my_list = [20, -3, 15, 2, -1, -21]
# list1=[x for x in my_list if x >= 0]
# print(list1)
#
# # 4.4
# # import functools
# from functools import reduce
# my_list = reduce(lambda x, y: x*y, list1)
# print(my_list)

#  # 4.5
# from lesson1_HW2 import *
# def tests():
#      assert sum_it(3, 4) == 7, f'Актуальный результат {sum_it(3,4)}'
#      assert minus_it(4, 3) == 1, f'Актуальный результат {minus_it(4,3)}'
#      assert prod(3, 4) == 12, f'Актуальный результат {prod(3,4)}'
#      assert div(4, 2) == 2, f'Актуальный результат {div(4,2)}'
# print(div(4, 0))
# print(minus_it(4, 3))
# print(sum_it(3, 4))
# print(prod(3, 4))
# tests()