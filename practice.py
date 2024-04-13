# while True:
#  response=input('say something')
#  if(response=='bye'):
#   break
# a=8
# b=10
# if(a is b):
#  print("yes both are same memory location ")
# else:
#  print("both are different location")
# picture=[
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [0,1,1,1,1,1,0],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]
# for image in picture:
#     for pixcel in image:
#         if(pixcel==1):
#             print(" * ", end=" ")
#         else:
#             print(" ")
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]

# for row in picture:
#     for pixel in row:
#         if pixel == 1:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ") 
#     print() 
# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
    
# print(is_even(51))

# def super_func(*args):
#     print (args)
#     return sum(args)
# print(super_func(1,2,3,4,5))
# Highest even number in list
# def high_even(li):
#     even=[]
#     for item in li:
#         if(item%2==0):
#             even.append(item)
#             # (item)
#     return max(even)
    
    
# print(high_even([12,3,6,8,10,18]))
# picture=[
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]
# for rows in picture:
#     for pixcel in rows:
#         if pixcel==1:
#             print("*", end ="")
#         else:
#             print(" ", end ="")
#     print(' ')
# def multiplyby_two(num1):
#     return num1*2
# def sum(num1, num2):
#     return num1+num2
# print(multiplyby_two(5))
# Class
# class my_detail:
#     def __init__(self, name, age, height, weight):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.weight=weight
# show=my_detail("laxmi", 25, 5, 50)
# print(show)

# class BigObject:
#     pass

# obj1 = BigObject()
# obj2 = BigObject()
# obj3 = BigObject()

# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(obj1))
# help(BigObject)
# help(list)
# class playcharacter:
#     def __init__(self, name,age):
#         self.name=name
#         self.age=age
#     def run(self):
#         print('run')
# player1=playcharacter('cindy',25)
# player2=playcharacter('tom',34)  
# print(player1) 
# print(player2)  
# print(player1.name)    
# class dog:
#     def __init__(self,name, age):
#       self.name=name
#       self.age=age
# dog1=dog('dog1', 5)
# dog2=dog('dog2',9)
# dog3=dog('dpg3',45)
# def oldest(*args):
#        return max(args)
# print(f'oldest dog name is {oldest(dog1.age, dog2.age, dog3.age)}')
# class playCharacter:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def shout(self):
#      pass
#     @classmethod
#     def adding_things(cls, num1, num2):
#      return num1+num2     
# # player3=playCharacter.adding_things
# print(playCharacter.adding_things(2, 3))    
# /
# /class playcharacter:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def run(self):
#         print('run')
#     def speak(self):
#         print(f'my name is {self.name} and i am {self.age} old')
# player1=playcharacter('laxmi',25)
# player1.speak()

# from functools import reduce

# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
# def prit_upper(my_pets1):
#   return (list((str.upper, my_pets1)))
# print(prit_upper(my_pets))


# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]
# def lidt(my_numbers1, my_strings ):
#    for i in my_numbers(my_numbers.len-1, -1, 0):
#       my_numbers1.append[i]

#    return (list(zip(my_numbers1,my_strings)))
# print(lidt(my_strings,my_numbers))
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]
# def reverse(reverse_num):
#     reverse_num1=[]
#     for i in range(len(my_numbers)-1,-1,-1):
#         reverse_num1.append(reverse_num[i])
#     return reverse_num1

# def lidt(my_numbers1, my_strings):
   
#     num2=reverse(my_numbers1)
#     return list(zip(num2, my_strings))


# print(lidt(my_numbers, my_strings))

# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]

# def reverse(reverse_num):
#     reversed_list = []
#     for i in range(len(reverse_num) - 1, -1, -1):
#         reversed_list.append(reverse_num[i])
#     return reversed_list

# def lidt(my_numbers1, my_strings):
#     num2 = reverse(my_numbers1)
#     return list(zip(num2, my_strings))

# print(lidt(my_numbers, my_strings))


# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]

# def lidt(my_strings, my_numbers):
#     return list(zip(my_strings, my_numbers))

# print(lidt(my_strings, my_numbers))

#3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
# passed_scores1=list(filter(lambda x:x>50, scores))
# print(passed_scores1)

# print(list(zip(my_pets,passed_scores1)))

# def prit_upper(my_pets1):
#     return list(map(str.upper, my_pets1))

# print(prit_upper(my_pets))


# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# import pdb
# def add(num1, num2):
#     pdb.set_trace()
#     return num1+num2
# print("output is",add(4, 'kjhfdskjhfds'))
# from time import time
# def performance(fun):
#     def wrapper(*args, **kwargs):
#         t1=time()
#         result=fun(*args, **kwargs)
#         t2=time()
#         print(f'took{t2-t1} s')
#         return result
#     return wrapper
# @performance
# def long_time():
#     print('1')
#     for i in range(10000000):
#       i*5
      
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(10000000)):
#         i*5
# long_time()
# long_time2()


# def performane(fun):
#     def wrapper(*args, **kwargs):
#         t1=time()
#         result=wrapper()

# def div(a,b):
#     print(a/b)
# def smart(func):
#     def inner(a,b):
#         if a>b:
#             a,b=b,a
#         return func(a,b)
#     return inner

# div(8,5)

# def percentage(a,b):
#     print(a%b)

# def smart(func):
#     def inner(a, b):
#         if a<b:
#          a= a%b
#         return a
#     return inner


# percentage(6,40)

# def special_for(iterable):
#     iterator=iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator))
#         except StopIteration:
# #             break
# # special_for([1,2,3])
# def fib(number):
#     a=0
#     b=1
#     for i in range(number):
#         yield a
#         temp=a
#         a=b
#         b=temp+b

# for x in fib(20):
#  print (x )   
# x="krkjf"
# # print(typeOf(a))

# # print(x.upper)  
# from utility import multiply, devide, max
# # from shoping import shopping_cart
# # print(shopping_cart.buy('apple'))
# print(devide(5,2))
# print(multiply(5,2))
# # print(max([1,2]))

# # print(__name__)
# import random
# # help(random)
# print(dir(random))
# import sys
# sys.argv
# from random import randint
# answer=randint(1,10)
# guess=input("enter the number 1~10")

# while True:
#     try:
#         if int(guess)>0 and int(guess)<11:
#             print("all good")
#             break
#     except ValueError:
#         print("please enter in between number")
#         continue
# import sys

# from random import randint

# random_number = randint(int(sys.argv[1]), int(sys.argv[2]))

# while True:
#     try:
#         number = int(
#             input('Please choose a number that falls between those two you just chose: '))
#         if number >= int(sys.argv[1]) and number <= int(sys.argv[2]):
#             if number == random_number:
#                 print("You're a genius!")
#                 break
#     except ValueError:
#         print("Please enter a number")
#         continue

# import pyjokes
# p1=pyjokes.get_joke('en', 'neutral')
# print(p1)
# from collections import Counter,defaultdict, OrderedDict
# li=[1,2,3,4,5,6,7,8] 
# sentance='jhgd agd laxmi bdnj diuaed ahd'
# print(Counter(li))
# print(Counter(sentance))
# import pdb
# def add(n1, n2):
#     pdb.set_trace()
#     t=6*7
#     return n1+n2
# add(4,'kierhtk')

# def do_stuff(num):
#     return num+5

import random
answer=random.randint(1, 10)
print(answer)
while True:
 try:
    guess=int(input("enter number in between 1 to 10"))
    if 0<guess<11:
        if guess==answer:
            print("you are a genius")
            break
        else:
            print('hey bozo, i said 1 to 10')
 except ValueError:
    print("please print a number")
    continue