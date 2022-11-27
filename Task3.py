x = int(input('X ≠ 0'))
y = int(input('Y ≠ 0'))
if x > 0 and y > 0:
    print('Точка находится в плоскости 1')
elif x < 0 and y > 0:
    print('Точка находится в плоскости 2')
elif x < 0 and y < 0:
    print('Точка находится в плоскости 3')
elif x > 0 and y < 0:
    print('Точка находится в плоскости 4')


