import numpy as np

from Glob_obrat import Glob_matrica_obrat
from Silovaya_nagruzka import silovaya_nagryzka

from gest_elem import gest_kagdogo_elem

from peremechenia import peremecheniya_v_uzlah


def scalar(a,b):
    """Скалярное произведение"""
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


if __name__ == '__main__':
    e = int(input("Введите число конечных элементов: е = "))
    f = float(input("Введите значение сосредоточенной силовой нагрузки: f = "))
    N_e = int(input("Введите номер элемента, к которому приложена нагрузка: N(е) = "))
    q = float(input("Введите значение распределённой силовой нагрузки: q = "))
    n_e = int(input("Введите номер элемента, содержащий начальную точку приложения : n_e = "))
    n_e_k = int(input("Введите номер элемента, содержащий конечную точку приложения : n_e_k = "))
    U = peremecheniya_v_uzlah(e, f, q, N_e, n_e, n_e_k)
    U = [x[0] for x in U]
    print('Суммарный вектор перемещений')
    print(U)
    for num_el in range(1, e + 1):
        print('-' * 30)
        peremech_elem(e, U, num_el, l=1)



