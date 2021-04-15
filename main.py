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
    print(K_EF_obr)
    return K_EF_obr


def dliny_elementov(name):
    L = []
    for i in range(e):
        L.append(int(input('Введите значение длины i-ого элемента: ')))
    print(L)
    return L

def silovaya_nagryzka(name):

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
    r = e + 1
    c = 1
    Q_s = []
    for i in range(r):
        Q_s.append([])
        for j in range(c):
            if ((i) >= (n_e - 1)) and ((i) <= (n_e_k)) and (n_e != n_e_k):
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


def silovsya_raspredel_nagryzka(name):
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


def peremecheniya(name):
    Glob = kolvo_elementov_i_gestkost_kagdogo_elementa(name)
    F = silovaya_nagryzka(name)
    U = Glob.dot(F)
    print('Суммарный вектор перемещений')
    print(U)
    return U



def funk_form(name):
    l = 1
    N = []
    for i in range(e+1):
        N.append([])
    for i in range(e+1):
        N[i] = []
    for i in range(e+1):
        N1 = 1 - x/l
        N2 = x/l
        N[i].append(N1)
        N[i].apeend(N2)
    print(N)
    return N


def scalar(a,b):
    return a[0]*b[0]+a[1]*b[1]


def approximation(x,u_e,l):
    N_1 = 1 - x / l
    N_2 = x / l
    N = [N_1, N_2]
    return scalar(N,u_e)


def peremech_elem(x,u,l):
    u_e = []
    for i in range(e+1):
        u_e.append([])
        u_e[i].append(U[i])
    print('x=0',approximation(0,u_e,1))
    print('x=0.25', approximation(0.25, u_e, 1))
    print('x=0.5', approximation(0.5, u_e, 1))
    print('x=0.75', approximation(0.75, u_e, 1))
    print('x=1', approximation(1, u_e, 1))


def vnut_ysil(name):
    N1_proiz = -1/l
    N2_proiz = 1/l
    N_proiz = [N1_proiz,N2_proiz]
    N_e = (N_proiz[0]*u_e[0]+N_proiz[1]*u_e[1])*K_EF_e
    print(N_e)



if __name__ == '__main__':
    e = int(input("Введите число конечных элементов: е = "))
    f = int(input("Введите значение сосредоточенной силовой нагрузки: f = "))
    N_e = int(input("Введите номер элемента, к которому приложена нагрузка: N(е) = "))
    q = int(input("Введите значение распределённой силовой нагрузки: q = "))
    l = int(input(
        "Введите значение длины, на которой приложена нагрузка. Число должно быть целым! Длина каждого элемента здесь равна 1: l = "))
    n_e = int(input("Введите номер элемента, содержащий начальную точку приложения : n_e = "))
    n_e_k = int(input("Введите номер элемента, содержащий конечную точку приложения : n_e_k = "))
    kolvo_elementov_i_gestkost_kagdogo_elementa('A')
    dliny_elementov('A')
    silovaya_nagryzka('A')
    silovsya_raspredel_nagryzka('A')
    peremecheniya('A')
    funk_form('A')
    vnut_ysil('A')
