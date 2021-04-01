import numpy as np

K_vsp = []

def kolvo_elementov_i_gestkost_kagdogo_elementa(name):

    K_vsp = []
    for k in range(e):
        K_vsp_1 = []
        ef = int(input("Введите значение жёсткости элемента (начения могут быть только натуральными числами): ef = "))
        r = 2
        c = 2
        K_EF_e = []
        for i in range(r):
            K_EF_e.append([])
            K_vsp_2 = []
            for j in range(c):
                if (i+j) % 2 == 0:
                    K_EF_e[i].append(ef)
                else:
                    K_EF_e[i].append(-ef)
                K_vsp_2.append(K_EF_e[i][j])
            K_vsp_1.append(K_vsp_2)
        K_vsp.append(K_vsp_1)
        for i in range(r):
            for j in range(c):
                print(K_EF_e[i][j], end=" ")
            print()
    print('Вспомогательная матрица: ')
    print(K_vsp)
    print('Глобальная матрица: ')
    K_EF = []
    for i in range(e+1):
        K_EF.append([])
    K_EF[0].append(K_vsp[0][0][0])
    for i in range(e+1):
        for j in range(e+1):
            if (i == j) and (i !=0) and (i != e):
                K_EF[i].append(K_vsp[i][0][0]+K_vsp[i-1][0][0])
            elif (j == i-1) and (i != 0):
                K_EF[i].append(K_vsp[i-1][0][1])
            elif (j == (i+1)):
                K_EF[i].append(K_vsp[i][0][1])
            elif (j != i) and (j != -1) and (i != -1):
                K_EF[i].append(0)
    K_EF[-1].append(K_vsp[-1][0][0])
    print(K_EF)
    print('Глобальная матрица жёсткости с учётом граничных условий по методу Пиано_Айренса: ')
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


def obr_Glob_matr_G(name):
    
    K_EF_obr = np.linalg.inv(K_EF)
    print(K_EF_obr)


def silovaya_sosredotoch_nagryzka(name):

    f = int(input("Введите значение сосредоточенной силовой нагрузки: f = "))
    N_e = int(input("Введите номер элемента, к которому приложена нагрузка: N(е) = "))
    r = e+1
    c = 1
    F_s = []
    for i in range(r):
        F_s.append([])
        for j in range(c):
            if (i) == (N_e-1):
                F_s[i].append(f)
            else:
                F_s[i].append(0)
    print("Число узлов системы на 1 больше числа конечных элементов. Номер узла, в котором приложена сила, совпадает с номером элемента, к которому она приложена.")
    print(F_s, sep = "\n")


def silovsya_raspredel_nagryzka(name):

    q = int(input("Введите значение распределённой силовой нагрузки: q = "))
    l = int(input("Введите значение длины, на которой приложена нагрузка. Число должно быть целым! Длина каждого элемента здесь равна 1: l = "))
    n_e = int(input("Введите номер элемента, содержащий начальную точку приложения : n_e = "))
    n_e_k = int(input("Введите номер элемента, содержащий конечную точку приложения : n_e_k = "))
    r = e + 1
    c = 1
    Q = []
    for i in range(r):
        Q.append([])
        for j in range(c):
            if (i) == (n_e - 1):
                Q[i].append(q)
            else:
                Q.append(0)
            if (i) == (n_e_k - 1):
                Q[i].append(q)
            else:
                Q.append(0)
    print("Число узлов системы на 1 больше числа конечных элементов. Номер узла, в котором приложена сила, совпадает с номером элемента, к которому она приложена.")
    print(Q, sep="\n")


if __name__ == '__main__':
    e = int(input("Введите число конечных элементов: е = "))
    kolvo_elementov_i_gestkost_kagdogo_elementa('A')
    silovaya_sosredotoch_nagryzka('A')
    silovsya_raspredel_nagryzka('A')
    obr_Glob_matr_G('F')

