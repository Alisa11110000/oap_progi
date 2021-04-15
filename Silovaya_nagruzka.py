import numpy as np


def silovaya_nagryzka(e,N_e,f,q,n_e,n_e_k):
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

if __name__ == '__main__':
    e = int(input("Введите число конечных элементов: е = "))
    f = int(input("Введите значение сосредоточенной силовой нагрузки: f = "))
    N_e = int(input("Введите номер элемента, к которому приложена нагрузка: N(е) = "))
    q = int(input("Введите значение распределённой силовой нагрузки: q = "))
    l = int(input(
        "Введите значение длины, на которой приложена нагрузка. Число должно быть целым! Длина каждого элемента здесь равна 1: l = "))
    n_e = int(input("Введите номер элемента, содержащий начальную точку приложения : n_e = "))
    n_e_k = int(input("Введите номер элемента, содержащий конечную точку приложения : n_e_k = "))
    silovaya_nagryzka(e,N_e,f,q,n_e,n_e_k)


