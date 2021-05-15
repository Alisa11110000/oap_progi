import numpy as np


from vvodniye_dlya_gestkosty import kolvo_elementov_i_gestkost_kagdogo_elementa


def Glob_matrica(e):
    K_vsp = kolvo_elementov_i_gestkost_kagdogo_elementa(e)
    print('Глобальная матрица жёсткости: ')
    K_EF = []
    for i in range(e + 1):
        K_EF.append([])
    K_EF[0].append(K_vsp[0][0][0])
    for i in range(e + 1):
        for j in range(e + 1):
            if (i == j) and (i != 0) and (i != e):
                K_EF[i].append(K_vsp[i][0][0] + K_vsp[i - 1][0][0])
            elif (j == i - 1) and (i != 0):
                K_EF[i].append(K_vsp[i - 1][0][1])
            elif (j == (i + 1)):
                K_EF[i].append(K_vsp[i][0][1])
            elif (j != i) and (j != -1) and (i != -1):
                K_EF[i].append(0)
    K_EF[-1].append(K_vsp[-1][0][0])
    print(K_EF)
    print('Глобальная матрица жёсткости с учётом граничных условий по методу Пиано_Айронса: ')
    for i in range(e + 1):
        for j in range(e + 1):
            if (i == 0) and (j != 0):
                K_EF[i][j] = 0
            elif (i == e) and (j != e):
                K_EF[i][j] = 0
            elif (j == 0) and (i != 0):
                K_EF[i][j] = 0
            elif (j == e) and (i != e):
                K_EF[i][j] = 0
    K_EF[0][0] = 1
    K_EF[-1][-1] = 1
    print(K_EF)
    return K_EF


if __name__ == '__main__':
    e = int(input("Введите число конечных элементов: е = "))
    Glob_matrica(e)
