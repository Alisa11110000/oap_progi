import numpy as np

from Glob_obrat import Glob_matrica_obrat
from Silovaya_nagruzka import silovaya_nagryzka


def dliny_elementov(name):
    L = []
    for i in range(e):
        L.append(int(input('Введите значение длины i-ого элемента: ')))
    print(L)
    return L


def peremecheniya(name):
    Glob = Glob_matrica_obrat(e)
    F = silovaya_nagryzka(e,N_e,f,q,n_e,n_e_k)
    U = Glob.dot(F)
    print('Суммарный вектор перемещений в узлах')
    print(U)


if __name__ == '__main__':
    e = int(input("Введите число конечных элементов: е = "))
    f = int(input("Введите значение сосредоточенной силовой нагрузки: f = "))
    N_e = int(input("Введите номер элемента, к которому приложена нагрузка: N(е) = "))
    q = int(input("Введите значение распределённой силовой нагрузки: q = "))
    n_e = int(input("Введите номер элемента, содержащий начальную точку приложения : n_e = "))
    n_e_k = int(input("Введите номер элемента, содержащий конечную точку приложения : n_e_k = "))
    silovaya_nagryzka(e,N_e,f,q,n_e,n_e_k)
    peremecheniya('A')
