import numpy as np

e = int(input("Введите число конечных элементов: е = "))
def colichestvo_elementov_i_gestkost_kagdogo_elementa(name):

    K_vsp = []
    for k in range(e):
        K_vsp_1 = []
        ef = int(input("Введите значение жёсткости элемента: ef = "))
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
    print(K_vsp)
    K_EF = []
    for k in range(e):
        K_EF[e].append(K_vsp_1[e])
        print(K_EF[e], end=" ")




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
    colichestvo_elementov_i_gestkost_kagdogo_elementa('PyCharm')
    silovaya_sosredotoch_nagryzka('PyCharm')
    silovsya_raspredel_nagryzka('PyCharm')
    globalnaya_matriza_gestkosri('PyCharm')

