#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
#Выведите минимальное количество монет, которые нужно перевернуть
import random
from random import randint
heads = 0
tails = 0
n = int(input())
i = 0
k = 0
while i != n:
   k = random_number = randint(0, 1)
   if k == 0: heads = heads+1
   elif k == 1: tails= tails +1
   i = i+1
if heads < tails:
   print(heads)
elif tails < heads:
   print(tails)
