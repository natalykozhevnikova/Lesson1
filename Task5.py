Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21




import math
import os
os.system('cls')
ax = float(input('Введите координату точки A по оси Х: '))
ay = float(input('Введите координату точки А по оси Y: '))
bx = float(input('Введите координату точки B по оси Х: '))
by = float(input('Введите координату точки B по оси Y: '))
distance = round(math.sqrt((bx-ax) ** 2 + (by -ay) ** 2):
    print(distance)




