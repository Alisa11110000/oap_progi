import numpy as np

def kolvo_elementov_i_gestkost_kagdogo_elementa(e):
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
    return K_vsp


if __name__ == '__main__':
    e = int(input("Введите число конечных элементов: е = "))
    kolvo_elementov_i_gestkost_kagdogo_elementa(e)

