Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет



x = int (input("Введите день недели от 1 до 7"))
if x > 5:
    print('Yes')
else:
    print('No')
