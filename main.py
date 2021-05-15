import numpy as np
import sys

f = open


def kolvo_elementov_i_gestkost_kagdogo_elementa(e):
    K_gestk_elem = []
    for i in range(e):
        ef = int(input("Введите значение жёсткости элемента (начения могут быть только натуральными числами): ef = "))
        K_gestk_elem.append(ef)
    print('Матрица жесткостей элементов: ')
    print(K_gestk_elem)
    return K_gestk_elem


def vspom_matriza_sobiraet_gestkosti_vseh_elem(e):

    K_vsp_EF = []
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
        K_vsp_EF.append(K_vsp_1)
        for i in range(r):
            for j in range(c):
                print(K_EF_e[i][j], end=" ")
            print()
    print('Вспомогательная матрица: ')
    print(K_vsp_EF)
    return K_vsp_EF

def globalnaya_matrica_gestkosti(e):

    K_vsp = vspom_matriza_sobiraet_gestkosti_vseh_elem(e)
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
    K_EF_obr = np.linalg.inv(K_EF)
    print('Матрица, обратная глобальной матрице жёсткости:')
    print(K_EF_obr)
    return K_EF_obr


def dliny_elementov(e):
    L = []
    for i in range(e):
        L.append(int(input('Введите значение длины i-ого элемента: ')))
    print(L)
    return L

def silovaya_nagryzka(e, f, q, N_e, n_e, n_e_k):

    r = e+1
    c = 1
    F_s = []
    for i in range(r):
        F_s.append([])
        for j in range(c):
            if i == N_e-1:
                F_s[i].append(f)
            else:
                F_s[i].append(0)
    print("Число узлов системы на 1 больше числа конечных элементов. Номер узла, в котором приложена сила, совпадает с номером элемента, к которому она приложена.")
    print(F_s, sep = "\n")
    r = e + 1
    c = 1
    Q_s = []
    for i in range(r):
        Q_s.append([])
        for j in range(c):
            if (i >= n_e - 1) and (i <= n_e_k) and (n_e != n_e_k):
                Q_s[i].append(q)
            elif ((i) >= (n_e - 1)) and ((i) <= (n_e_k)) and (n_e == n_e_k):
                Q_s[i].append(q)
            else:
                Q_s[i].append(0)
    print(
        "Число узлов системы на 1 больше числа конечных элементов. Номер узла, в котором приложена сила, совпадает с номером элемента, к которому она приложена.")
    print(Q_s, sep="\n")
    F = []
    print('Суммарный вектор силовой нагрузки: ')
    for i in range(e+1):
        F.append([])
        for j in range(c):
            F[i].append(F_s[i][0]+Q_s[i][0])
    print(F)
    return F


def silovsya_raspredel_nagryzka(e):
    r = e + 1
    c = 1
    Q_s = []
    for i in range(r):
        Q_s.append([])
        for j in range(c):
            if ((i) >= (n_e-1)) and ((i) <= (n_e_k)) and (n_e != n_e_k):
                Q_s[i].append(q)
            elif ((i) >= (n_e-1)) and ((i) <= (n_e_k)) and (n_e == n_e_k):
                Q_s[i].append(q)
            else:
                Q_s[i].append(0)
    print("Число узлов системы на 1 больше числа конечных элементов. Номер узла, в котором приложена сила, совпадает с номером элемента, к которому она приложена.")
    print(Q_s, sep="\n")
    return Q_s


def peremecheniya(e, f, q, N_e, n_e, n_e_k):
    Glob = globalnaya_matrica_gestkosti(e)
    F = silovaya_nagryzka(e, f, q, N_e, n_e, n_e_k)
    U = Glob.dot(F)
    return U

def scalar(a,b):
    return a[0]*b[0]+a[1]*b[1]

def peremech_elem_x(e, U, num_el, x, l=1):
    if num_el < 1 or num_el > e:
        print("Неверный номер номер элемента")
        exit(1)
    N1 = 1 - x / l
    N2 = x / l
    N = [N1, N2]
    u1 = U[num_el-1]
    u2 = U[num_el]
    u = [u1, u2]
    return scalar(N, u)


def peremech_elem(e, U, num_el, l=1):
    print("Элемент №", num_el)
    for i in range(5):
        coord = 0.25*i*l
        u = peremech_elem_x(e, U, num_el, coord, l=l)
        print(f'x={0.25*i:4.2f} u={u:6.3f}')


def vnut_usil(e, U, num_el, x, l=1):
    if num_el < 1 or num_el > e:
        print("Неверный номер номер элемента")
        exit(1)
    EF_K = kolvo_elementov_i_gestkost_kagdogo_elementa(e)
    N1_proiz = - 1 / l
    N2_proiz = 1 / l
    N_proiz = [N1_proiz, N2_proiz]
    u1 = U[num_el - 1]
    u2 = U[num_el]
    u = [u1, u2]
    return scalar(N_proiz, u)*EF_K[num_el-1]


def vnut_ysiliya(e, U, num_el, l=1):
    print("Элемент №", num_el)
    for i in range(5):
        coord = 0.25 * i * l
        N_elem = vnut_usil(e, U, num_el, coord, l=1)
        print(f'x={0.25 * i:4.2f} N_elem={N_elem:6.3f}')


if __name__ == '__main__':
    e = int(input("Введите число конечных элементов: е = "))
    f = float(input("Введите значение сосредоточенной силовой нагрузки: f = "))
    N_e = int(input("Введите номер элемента, к которому приложена нагрузка: N(е) = "))
    q = float(input("Введите значение распределённой силовой нагрузки: q = "))
    l = int(input(
        "Введите значение длины, на которой приложена нагрузка. Число должно быть целым! Длина каждого элемента здесь равна 1: l = "))
    n_e = int(input("Введите номер элемента, содержащий начальную точку приложения : n_e = "))
    n_e_k = int(input("Введите номер элемента, содержащий конечную точку приложения : n_e_k = "))
    kolvo_elementov_i_gestkost_kagdogo_elementa(e)
    vspom_matriza_sobiraet_gestkosti_vseh_elem(e)
    globalnaya_matrica_gestkosti(e)
    dliny_elementov(e)
    silovaya_nagryzka(e, f, q, N_e, n_e, n_e_k)
    U = peremecheniya(e, f, q, N_e, n_e, n_e_k)
    print(U)
    U = [x[0] for x in U]
    print('Суммарный вектор перемещений')
    print(U)
    for num_el in range(1, e+1):
        print('-'*30)
        peremech_elem(e, U, num_el, l=1)
    for num_el in range(1, e+1):
        print('Усилия в элементе:')
        print('-' * 30)
        vnut_ysiliya(e, U, num_el, l)
