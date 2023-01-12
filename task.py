#Написать программу, которая из имеющегося массива строк, формирует массив из строк, длинна которых меньше или равна 3 символа. 

def input_array():
    array = input(f'Введите элементы массива через запятые\n').split(',')
    return array

def form_array():
    array = input_array()
    size = len(array)
    array_new = []
    for index in range (0,size):
        if len(array[index]) <= 3:
            array_new.append(array[index])
    print (array_new)
form_array()

