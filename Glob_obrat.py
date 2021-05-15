import numpy as np


from Glob_Gestk_i_dlina import Glob_matrica


def Glob_matrica_obrat(e):
    K_EF = Glob_matrica(e)
    K_EF_obr = np.linalg.inv(K_EF)
    print('Матрица, обратная глобальной матрице жёсткости: ')
    print(K_EF_obr)
    return K_EF_obr


if __name__ == '__main__':
    e = int(input("Введите число конечных элементов: е = "))
    Glob_matrica_obrat(e)

