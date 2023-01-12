#Написать программу, которая из имеющегося массива строк, формирует массив из строк, длинна которых меньше или равна 3 символа. 

def form_array():
    array = ["Hello", "2", "world", ":-)"]
    size = len(array)
    array_new = []
    index = 0
    for index in range (0,size):
        if len(array[index]) <= 3:
            array_new.append(array[index])
    index += 1
    print (array_new)
form_array()
