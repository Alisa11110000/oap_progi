import numpy as np


from peremechenia import peremecheniya_v_uzlah

from gest_elem import gest_kagdogo_elem


def scalar(a,b):
    return a[0]*b[0]+a[1]*b[1]


def vnut_usil(e, U, num_el, x, l=1):
    if num_el < 1 or num_el > e:
        print("Неверный номер номер элемента")
        exit(1)
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
    n_e = int(input("Введите номер элемента, содержащий начальную точку приложения : n_e = "))
    n_e_k = int(input("Введите номер элемента, содержащий конечную точку приложения : n_e_k = "))
    U = peremecheniya_v_uzlah(e, f, q, N_e, n_e, n_e_k)
    # приведём к массиву
    U = [x[0] for x in U]
    print('Суммарный вектор перемещений')
    print(U)
    for num_el in range(1, e+1):
        EF_K = gest_kagdogo_elem(e)
        print('Усилия в элементе:')
        print('-' * 30)
        vnut_ysiliya(e, U, num_el, l=1)