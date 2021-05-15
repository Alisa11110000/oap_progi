import numpy as np

def gest_kagdogo_elem(e):
    K_gestk_elem = []
    for i in range(e):
        ef = int(input("Введите значение жёсткости элемента (начения могут быть только натуральными числами): ef = "))
        K_gestk_elem.append(ef)
    print('Матрица жесткостей элементов: ')
    print(K_gestk_elem)
    return K_gestk_elem


if __name__ == '__main__':
    e = int(input("Введите число конечных элементов: е = "))
    gest_kagdogo_elem(e)


