#Задача 1
name=int(input("Сколько вам лет?:"))
if name>18:
    print("Доступ разрешен")
else:
    print("Извините, пользоваться данным ресурсом можно только с 18 лет")

#Задача 2
n=int(input("введите число"))
if  21>n>0:
   for n in range(0,21):
    
      if n%2==0:
         print(n, "это четное число")
      elif n%2!=0:
          print(n,"это нечетнок число")
else:
    print("я не понимаю чего вы от меня хотите.")
    
#Задача 3
number = input('Введите число ') #например 58375
print(max(number))

#homework_leson3_easy
#задача 1
fruits=['apple','banan','mango','orange']
fruit=len(fruits)
for i in range(fruit):
    print(str(i+1)+'.'+'{}'.format(fruits[i]))
#задача 2
a = {'1', '2', '3', '4', '5', '6'}
b = {'1', '2', '3', '4'}
c = a - b
print(list(c))
#задача 3
one_list=[2,3,4,5,6,8,10,12]
new_list=[]
two_list=len(one_list)
for i in range(two_list):
    if one_list[i]%2==0:
        new_list.append(one_list[i]/4)
    else:
        new_list.append(one_list[i]*2)
print(new_list)
#homework_lesson3_nomal
#задача1

import math
one_list=[2,-5,8,9,-25,25,4]
new_list=[]
for i in one_list:
    if i >0 and math.sqrt(i)%1==0:
        new_list.append(int(math.sqrt(i)))
print(new_list)

#задача 3

import random
n=int(input("введи количество элементов"))
new1_list=[]
for a in range(n):
    new1_list.append(random.randint(-100,100))
print(new1_list)

#задача 4
one_list=[1,2,4,5,6,2,5,2]
new_list=set(one_list)
print(new_list)

