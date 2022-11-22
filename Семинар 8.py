import random
import math

def PrintMatrix(numbers):
    for row in numbers:
        print(row)


def Task1():
    # Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки
    # заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с
    # наилучшим средним баллом.
    
    rows = 10     # 10 групп студентов
    numbers = [0]*rows

    for i in range(rows):
        cols = random.randint(20, 30)
        numbers[i] = list(random.randint(1, 5) for j in range(cols))
    PrintMatrix(numbers)

    sr_ball = list(sum(row)/len(row) for row in numbers)
    print(f"Группа с лучшим средним баллом {sr_ball.index(max(sr_ball))+1}")

def Task2():
    # Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите,
    # сумма элементов каких строк превосходит сумму главной диагонали матрицы.

    rows = random.randint(3,10)
    numbers = [0]*rows
    for i in range(rows):
        numbers =list( list(random.randint(1, 5) for j in range(rows)) for i in range(rows))

    PrintMatrix(numbers)
    gl_sum = sum(list( numbers[i][i] for i in range(rows)))  # сумма главной диагонали
    row_sum = list(map(lambda x: x > gl_sum,  list(sum(row) for row in numbers)))  # содержит true,если сумма соответствующей строки больше гл. диагонали 
    result = [i for i in range(rows) if row_sum[i] == True]
    print(f"Строки, превосходящие главную диагональ:{result}" if len(result) > 0 else "Нет сторок превосходящих главную дагональ")

def PrintData(num):
    days = [31, 30, 31, 31, 30]
    months = ["05", "06", "07", "08", "09"]    
    sum = 0
    for i in range(len(days)):
        sum += days[i]
        if sum >= num + 1:
            return str(days[i] - (sum - num - 1)) + "." + months[i]


def Task3():
    temper = [0]*5
    days = [31, 30, 31, 31, 30]
    months = ["05", "06", "07", "08", "09"]
    # зададим температуры случайным образом 
    for i in range(len(months)):
        temper[i] = list(random.randint(5, 35) for _ in range(days[i]))

    PrintMatrix(temper)
    # переведем в одномерный массив
    temp =[]
    for rows in temper:
        for el in rows:
            temp.append(el)
    
    min_temt = sum(temp[0:6])/7
    min_index = 0
    max_temp = sum(temp[0:6])/7
    max_index = 0
    for i in range(len(temp)-7):
        if sum(temp[i:i+7])/7 < min_temt:
            min_temt = sum(temp[i:i+7])/7
            min_index = i
        if sum(temp[i:i+7])/7 > max_temp:
            max_temp = sum(temp[i:i+7])/7
            max_index = i
    print(f"Самый холодный период: {PrintData(min_index)} - {PrintData(min_index + 6)}")
    print(f"Самый жаркий период: {PrintData(max_index)} - {PrintData(max_index + 6)}")


Task3()